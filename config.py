from pytest_html import extras,plugin
from py.xml import html
import re
def rootPath():
    name= __name__
    path=__file__
    return __file__.replace(name+".py","")
def summary_modification(prefix,summary,postfix):
    try:
        
        summary.extend ([html.p('')]) #do not comment this line, position of pie chart is depends on this empty string we are inserting
        #style=html.style(border='1px solid black')
        #table_1 = html.div( class_="pie",style="height: 100px;width:100px;border-radius: 50%;background: conic-gradient(brown 0.00%, black 0.00% 0.55%, blue 0.55% 6.08%, green 6.08% 13.68%, yellow 13.68% 23.27%, orange 23.27% 40.47%, red 40.47%)")
        

        
        pass_testcases=0
        failed_testcase=0
        skipped_testcase=0
        error_testcases=0

        for i in summary:
            #print(i,    '<---loop--')
            
            if 'py._xmlgen.span' in str(type(i)) :
                if '<span class="skipped">' in str(i):
                    skipped_testcase=int(re.findall(r'\d+', str(i))[0])
                if '<span class="failed">' in str(i):
                    failed_testcase=int(re.findall(r'\d+', str(i))[0])
                if '<span class="passed">' in str(i):
                    pass_testcases=int(re.findall(r'\d+', str(i))[0])
                if '<span class="error">' in str(i):
                    error_testcases=int(re.findall(r'\d+', str(i))[0])                
        total_cases=pass_testcases+failed_testcase+skipped_testcase+error_testcases


        failed = 0 if failed_testcase == 0 else (failed_testcase/total_cases)
        errorcases = 0 if error_testcases == 0 else (error_testcases/total_cases)
        passed = 0 if pass_testcases == 0 else (pass_testcases/total_cases)
        skipped = 0 if skipped_testcase == 0 else (skipped_testcase/total_cases)

        data_pie=html.link( rel='stylesheet',href='report_styles/summarypiechart.css')
        data_pie.append(html.div( class_="pie",style="--val_1:"+str(failed)+"; --val_2:"+str(passed)+"; --val_3:"+str(skipped)+"; --val_4:"+str(errorcases)))
        Data_table=html.div(class_="Container",style="float: right;position: relative;left: -70%;padding: 0 70px;line-height: 200%;")
        Data_table.append(html.ul())
        Data_table.append(html.li("pass %: "+str((pass_testcases/total_cases)*100),style="color: green;font-size: 12px;align-content: center;"))
        Data_table.append(html.li("fail %: "+str((failed_testcase/total_cases)*100),style="color: red;font-size: 12px;align-content: center;"))
        Data_table.append(html.li("skip %: "+str((skipped_testcase/total_cases)*100),style="color: orange;font-size: 12px;align-content: center;"))
        Data_table.append(html.li("error %: "+str((error_testcases/total_cases)*100),style="color: red;font-size: 12px;align-content: center;"))
        summary.extend ([data_pie,Data_table])
    except Exception as error:
        raise error        