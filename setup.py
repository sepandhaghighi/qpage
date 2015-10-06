import os
work_dir= os.getcwd()
image_dir = work_dir+"\\image"
doc_dir=work_dir+"\\doc"
out_dir=work_dir+"\\output"
page_name=["Home","Resume","Project","About Me"]
actual_name=["index","resume","project","about"]
def menu_maker():
    result=""
    for i in range(len(page_name)):
        
        result=result+'\t<a href="'+actual_name[i]+'.html">'+page_name[i]+"</a>\n"
        result=result+"&nbsp\n"
        
    result=result+"\t\t<hr></hr>\n"
    for i in range(len(page_name)):
        file=open(out_dir+"\\"+actual_name[i]+".html","a")
        file.write(result)
        file.close()
        
def html_init(name):
    html_name= out_dir+"\\"+name+".html"
    file=open(html_name,"w")
    file.write("<html>\n")
    file.write("\t<head>\n")
    if name=="index":
        file.write("\t\t<title>Welcome To My Homepage</title>\n")
    else:
        file.write("\t\t<title>"+name.upper()+"</title>\n")
    file.write("\t</head>\n")
    file.write("\t<body>\n")
    file.close()
def html_end(name):
    html_name= out_dir+"\\"+name+".html"
    file=open(html_name,"a")
    file.write("\t</body>\n")
    file.write("</html>")
    file.close()
def contain(name):
    try:
        image_code=""
        text_code=""
        file=open(out_dir+"\\"+name+".html","a")
        if name=="index":
            image_code=image_code+'<center><img src="image.jpg" , width=250px></img></center>\n'
            text_file=open(doc_dir+"\\"+name+".txt","r")
            text=text_file.read()
            text_file.close()
            text_code="<h3>"+text+"</h3>\n"
            file.write(image_code)
            file.write(text_code)
            file.close()
        else:
            text_file=open(doc_dir+"\\"+name+".txt","r")
            text=text_file.read()
            text_file.close()
            text_code="<h3>"+text+"</h3>\n"
            file.write(text_code)
            file.close()
    except:
        print ("Error In Text File Read Of "+name.upper()+" Page")
        print(" Please Insert Text File With Page Name In doc folder ")
        
        


if __name__=="__main__":
    for i in actual_name:
        html_init(i)
    menu_maker()
    
    for i in actual_name:
        contain(i)
        html_end(i)
    
    

