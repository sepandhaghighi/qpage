import os
import datetime

IP_FINDER_API = "http://ipinfo.io/ip"
SERVER_API = "http://sepkjaer.pythonanywhere.com/install"
SOURCE_DIR = os.getcwd()  # Get Current Directory
RESOURCE_DIR = os.path.join(os.pardir, 'resource')
IMAGE_DIR = os.path.join(SOURCE_DIR, 'image')
DOC_DIR = os.path.join(SOURCE_DIR, 'doc')
OUT_DIR = os.path.join(SOURCE_DIR, 'output')
FONT_DIR = os.path.join(SOURCE_DIR, 'font')
SAMPLE_DICT_ADDR = {os.path.join(IMAGE_DIR, "profile.png"): "http://www.qpage.ir/sample/profile.png",
                    os.path.join(FONT_DIR, "font.TTF"): "http://www.qpage.ir/sample/font.TTF",
                    os.path.join(DOC_DIR, "resume.pdf"): "http://www.qpage.ir/sample/resume.pdf",
                    os.path.join(DOC_DIR, "resume.txt"): "http://www.qpage.ir/sample/resume.txt",
                    os.path.join(IMAGE_DIR, "icon.ico"): "http://www.qpage.ir/sample/icon.ico"}
SAMPLE_DICT_MESSAGE = ["Profile Image", "Font", "Resume Part-1", "Resume Part-2", "Icon File"]
BADGE_COLOR_LIST = ["brightgreen", "green", "yellowgreen", "yellow", "orange", "red", "lightgrey", "blue"]
IMAGE_COUNTER = 0
PDF_COUNTER = 0
SPACE = "&nbsp\n"

PAGE_NAME = ["Home"]  # list of default HOMEPAGE Name
ACTUAL_NAME = ["index"]  # List of Actual Name Like Home.Html
BREAK_LINE = "<hr/><hr/>\n"
HOMEPAGE = "http://www.qpage.ir"
VERSION = "1.9"
ADV_BADGE_STATIC = "https://img.shields.io/badge/"
ERROR_DICT = {"image_error": "[Error-1001]", "resume_error": "[Error-1002]", "firstpage_error": "[Error-1003]",
              "empty_error": "[Error-1004]"}
WARNING_DICT = {"icon_warning": "[Warning-2001]", "font_warning": "[Warning-2002]", "color_warning": "[Warning-2003]"}
COLOR_BOX = ["White", "Black", "Purple", "Yellow", "Orange", "Green", "Blue"]  # Color list for background and text
SIZE_BOX = ["50px", "100px", "200px", "360px", "500px"]  # list of size of images
IMFORMAT_BOX = ["jpg", "bmp", "png", "gif", "tiff", "JPG", "BMP", "PNG", "GIF",
                "TIFF"]  # list of supported image format
FONTSTYLE_BOX = ["normal", "italic", "oblique"]
FONT_FORMAT = [".ttf", ".woff", ".svg", ".eot"]
TARGET_BLANK = 'target="blank"'
CSS_MARGIN = '''margin-top: 50px;
    margin-bottom: 50px;
    margin-right: 50px;
    margin-left: 50px;
    border : 10px groove white;
    padding-top:10px;
    padding-bottom:20px;
    padding-left:10px;
    padding-right:10px;
    '''
CSS_ANIMATION_1 = '''
   animation-name: anim1;
    animation-duration: 4s;
    animation-fill-mode: both;
'''
CSS_ANIMATION_2 = '''
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
