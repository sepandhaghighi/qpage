import os
import datetime

work_dir = os.getcwd()  # Get Current Directory
image_dir = os.path.join(work_dir, 'image')
doc_dir = os.path.join(work_dir, 'doc')
out_dir = os.path.join(work_dir, 'output')
font_dir = os.path.join(work_dir, 'font')
page_name = ["Home"]  # list of default Homepage Name
actual_name = ["index"]  # List of Actual Name Like Home.Html
break_line = "<hr/><hr/>\n"
homepage = "http://www.qpage.ir"
version = "V1.8"
color_box = ["White", "Black", "Purple", "Yellow", "Orange", "Green", "Blue"]  # Color list for background and text
size_box = ["50px", "100px", "200px", "360px", "500px"]  # list of size of images
imformat_box = ["jpg", "bmp", "png", "gif", "tiff"]  # list of supported image format
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
files = []
warnings = []
today_time = str(datetime.date.today())  # Get Today Date By datetime module
