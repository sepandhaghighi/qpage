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
    return result
def menu_writer():
    message=menu_maker()
    for i in range(len(page_name)):
        file=open(out_dir+"\\"+actual_name[i]+".html","a")
        file.write(message)
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
def print_text(text_file,file):
    text_code=""
    header_start="<h4>"
    header_end="</h4>\n"
    space="&nbsp\n"
    for line in text_file:
        line.strip()
        text=line
        if len(line)==1:
            text_code=space
        else:
            if line.find("[L]")!=-1:
                header_start="<h2>"
                header_end="</h2>\n"
                text=line[3:]
            elif line.find("[S]")!=-1:
                header_start="<h5>"
                header_end="</h5>\n"
                text=line[3:]
            elif line.find("[M]")!=-1:
                text=line[3:]
            text_code=header_start+text+header_end
        file.write(text_code)
        
    file.close()
def print_image(file,close=False):
    image_code='<center><img src="image.jpg" , width=250px></img></center>\n'
    file.write(image_code)
    if close==True:
        file.close()
def contain(name):
    try:
        image_code=""
        
        file=open(out_dir+"\\"+name+".html","a")
        text_file=open(doc_dir+"\\"+name+".txt","r")
        if name=="index":
            print_image(file)
            print_text(text_file,file)
        else:
            print_text(text_file,file)
            
    except:
        print ("Error In Text File Read Of "+name.upper()+" Page")
        print(" Please Insert Text File With Page Name In doc folder ")
        
        


if __name__=="__main__":
    try:
        for i in actual_name:
            html_init(i)
        menu_writer()
    
        for i in actual_name:
            contain(i)
            html_end(i)
        print("Homepage is ready")
        print("Upload out and image folder contains directly to your host")
        print("Please Dont Change HTML Files Name")
    except:
        print ("Error In Creating HTML Files")
    
    

