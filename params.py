import os
import datetime
work_dir = os.getcwd()  # Get Current Directory
image_dir = os.path.join(work_dir, 'image')
doc_dir = os.path.join(work_dir, 'doc')
out_dir = os.path.join(work_dir, 'output')
font_dir = os.path.join(work_dir, 'font')
sample_dict_addr={os.path.join(image_dir,"profile.png"):"http://www.qpage.ir/sample/profile.png",os.path.join(font_dir,"font.TTF"):"http://www.qpage.ir/sample/font.TTF",os.path.join(doc_dir,"resume.pdf"):"http://www.qpage.ir/sample/resume.pdf",os.path.join(doc_dir,"resume.txt"):"http://www.qpage.ir/sample/resume.txt",os.path.join(image_dir,"icon.ico"):"http://www.qpage.ir/sample/icon.ico"}
sample_dict_message=["Profile Image","Font","Resume Part-1","Resume Part-2","Icon File"]
badge_color_list=["brightgreen","green","yellowgreen","yellow","orange","red","lightgrey","blue"]
image_counter = 0
pdf_counter = 0
space = "&nbsp\n"


page_name = ["Home"]  # list of default Homepage Name
actual_name = ["index"]  # List of Actual Name Like Home.Html
break_line = "<hr/><hr/>\n"
homepage = "http://www.qpage.ir"
version = "1.9"
adv_badge_static="https://img.shields.io/badge/"

color_box = ["White", "Black", "Purple", "Yellow", "Orange", "Green", "Blue"]  # Color list for background and text
size_box = ["50px", "100px", "200px", "360px", "500px"]  # list of size of images
imformat_box = ["jpg", "bmp", "png", "gif", "tiff","JPG","BMP","PNG","GIF","TIFF"]  # list of supported image format
fontstyle_box = ["normal", "italic", "oblique"]
font_format = [".ttf", ".woff", ".svg", ".eot"]
target_blank = 'target="blank"'
css_margin = '''margin-top: 50px;
    margin-bottom: 50px;
    margin-right: 50px;
    margin-left: 50px;
    border : 10px groove white;
    padding-top:10px;
    padding-bottom:20px;
    padding-left:10px;
    padding-right:10px;
    '''
css_animation_1='''
   animation-name: anim1;
    animation-duration: 4s;
    animation-fill-mode: both;
'''
css_animation_2='''
@keyframes anim1{
    0%{opacity: 0;}
    25%{opacity: 0.4;}
    50%{opacity:0.5;}
    75%{opacity:0.7;}
    100%{opacity: 1;}

}


'''
files = []
warnings = []
today_time = str(datetime.date.today())  # Get Today Date By datetime module
