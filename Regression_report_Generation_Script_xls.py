#library
import re 
import os
import xlwt
from tkinter import filedialog,Tk

#excel initalization
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("regression_report_generateion1")
sheet2 = book.add_sheet("regression_report_generateion")

root = Tk()
selected_file =  filedialog.askopenfilenames(title = "Select file",filetypes = (("log files","*.log"),("sv files","*.sv"),("all files","*.*")))

#excel header
sheet1.write(0, 0, "file_name")
sheet1.write(0, 1, "error_count")
sheet1.write(0, 2, "fatal_count")
sheet1.write(0, 3, "status")

style_pass = xlwt.easyxf('pattern: pattern solid, fore_colour green;')
style_fail = xlwt.easyxf('pattern: pattern solid, fore_colour red;')

sheet2.write(0, 0, "file_name")
sheet2.write(0, 1, "error_count")
sheet2.write(0, 2, "fatal_count")
sheet2.write(0, 3, "status")
style_pass = xlwt.easyxf('pattern: pattern solid, fore_colour green;')





passrow=0
failrow=0
for each_file in selected_file:
    print(each_file)
    each_file=os.path.basename(each_file)
    fh=open(each_file,"r")
    for fc in fh:
        error=re.match("UVM_ERROR\s:\s+(.*)",fc)
        fatal=re.match("UVM_FATAL\s:\s+(.*)",fc)
        if error:
            error_count=error.group(1)
            print(error_count)
        if fatal:
            fatal_count=fatal.group(1)
            print(fatal_count)
    if((int(error_count)==0) & (int(fatal_count)==0)):
        status="pass"
    else:
       status="fail" 

    if status=="pass":
        passrow=passrow+1
        sheet1.write(passrow, 0, each_file)
        sheet1.write(passrow, 1, error_count)
        sheet1.write(passrow, 2, fatal_count)
   
    if status == "pass":
        sheet1.write(passrow, 3, status,style=style_pass)

    if status=="fail":    
        failrow=failrow+1
        sheet2.write(failrow, 0, each_file)
        sheet2.write(failrow, 1, error_count)
        sheet2.write(failrow, 2, fatal_count)
     

    if status == "fail":
         sheet2.write(failrow, 3, status,style=style_fail)
book.save("trial3.xls")


