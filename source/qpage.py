import shutil  # Library For Work With File In High Level Like Copy
import webbrowser
from params import *
import socket
import requests
import re
import time
import sys
import urllib.request
import platform
import random
import datetime
from functools import reduce
import doctest
meta_input = ""


def show_items(enum_list):
    """ show item of enum_list
    :param enum_list the list that should be shown
    :type enum_list : list
    """
    for i, item in enumerate(enum_list):
        print(str(i + 1) + "-" + item)


def print_logo(external=False):
    '''
    print qpage logo by sequential characters
    :param external: flag for choosing internal or external logo
    :type external:bool
    :return: None
    >>> print_logo()
      ____    ___
     / __ \  / _ \___ ____ ____
    / /_/ / / ___/ _ `/ _ `/ -_)
    \___\_\/_/   \_,_/\_, /\__/
                     /___/
    '''
    if external==True:
        if "logo.txt" in os.listdir(RESOURCE_DIR):
            logo_path = os.path.join(RESOURCE_DIR, 'logo.txt')
            with open(logo_path, "r") as logo_file:
                for line in logo_file:
                    print(line.rstrip())
        else:
            pass
    else:
        print(LOGO)


def convert_bytes(num):
    """ convert num to idiomatic byte unit

    :param num: the input number.
    :type num:int
    :return: str
    >>> convert_bytes(200)
    '200.0 bytes'
    >>> convert_bytes(6000)
    '5.9 KB'
    >>> convert_bytes(80000)
    '78.1 KB'
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size():
    """ Print the size of output file
        :return: None
        >>> file_size() # if there is no output directory
        Access Error
        >>> file_size() # if there is a valid output directory
        Used SPACE --> 78.1 KB
    """
    try:
        list_of_files = os.listdir(OUT_DIR)
        response = 0
        for file in list_of_files:
            file_info = os.stat(os.path.join(OUT_DIR, file))
            response += file_info.st_size
        print_line(70, "*")
        print("Used SPACE --> " + convert_bytes(response))
        print_line(70, "*")
    except:
        print("Access Error!")


def download_badge(address):

    """ Download badge for website
    :param address: the address that should get badge
    :type address : str
    :return: None
    """
    r = requests.get(address, stream=True)
    with open(os.path.join(OUT_DIR, "badge.svg"), 'wb') as f:
        shutil.copyfileobj(r.raw, f)


def random_badge_color():
    """return a random color for badge
    :return: badge color as string
    >>> random.seed(1)
    >>> random_badge_color()
    'yellowgreen'
    """
    random_index = random.randint(0, len(BADGE_COLOR_LIST) - 1)
    return BADGE_COLOR_LIST[random_index]


def system_details():
    """
    Show detail of system that code is runnig on
    :return: system details as string (node , processor , platform)
    >>> system_details()
    'DESKTOP-B16C9BR , Intel64 Family 6 Model 94 Stepping 3, GenuineIntel ,  Windows-10-10.0.10240-SP0'
    """
    return platform.node() + " , " + platform.processor() + " ,  " + platform.platform()


def generation_time(time_1=None):
    """ Calculate the generation time

    :param time_1: time that passed but not counted in generation time
    :type time_1:float
    :return :the amount of time that passed  as float
    """
    if time_1 is None:
        return time.perf_counter()
    else:
        return time.perf_counter() - time_1


def find_global_ip():
    """ Find the global IP for using in API
    :return: return the IP as string
    """
    try:
        response = requests.get(IP_FINDER_API)
        return response.text[:-1]
    except Exception as e:
        error_log(e)
        return "0.0.0.0"


def create_badge(subject="qpage", status=VERSION, color="blue", random=False):
    '''
    this function use shields.io template for creating  badges
    :param subject: badge subject
    :param status: badge status ( in our case version)
    :param color: badge color
    :param random: randomization flag
    :type subject:str
    :type status:str
    :type color:str
    :type random:bool
    :return: shields.io badge addresses as string
    >>> create_badge()
    'https://img.shields.io/badge/qpage-1.9-blue.svg'
    >>> random.seed(1)
    >>> create_badge(random=True)
    'https://img.shields.io/badge/qpage-1.9-yellowgreen.svg'
    '''
    if random:
        color = random_badge_color()
    else:
        if color not in BADGE_COLOR_LIST:
            color = "orange"
    badge_adr = ADV_BADGE_STATIC + subject + "-" + status + "-" + color + '.svg'
    return badge_adr


def is_sample_downloaded():
    """ Check the sample site material is downloaded of not
    :return : index of materials that downloaded as list
    """
    download_list = []
    if "profile.png" not in os.listdir(IMAGE_DIR):
        download_list.append(0)
    if "font.TTF" not in os.listdir(FONT_DIR):
        download_list.append(1)
    if "resume.pdf" not in os.listdir(DOC_DIR) and "resume.txt" not in os.listdir(DOC_DIR):
        download_list.extend([2, 3])
    if "icon.ico" not in os.listdir(IMAGE_DIR):
        download_list.append(4)
    return download_list


def download_lorem():
    """ Download the lorem file
    :return: None
    """
    if internet():
        lorem_path = os.path.join(RESOURCE_DIR, 'Latin-Lipsum.txt')
        urllib.request.urlretrieve("http://www.qpage.ir/sample/Latin-Lipsum.txt", lorem_path)
    else:
        print("Error In Download Lorem")


def read_lorem(char=100):
    """ find and read lorem
    :param char: the amount of char that needed to print
    :type char:int
    :return : the lorem string
    >>> read_lorem(5)
    'Lorem ipsum dolor sit amet,'
    """
    try:
        if "Latin-Lipsum.txt" not in os.listdir(RESOURCE_DIR):
            download_lorem()
        lorem_path = os.path.join(RESOURCE_DIR, 'Latin-Lipsum.txt')
        lorem_file = open(lorem_path, "r")
        lorem_text = lorem_file.read()
        lorem_file.close()
        return " ".join(lorem_text.split(" ")[:char])
    except Exception as e:
        error_log(e)
        return None


def sample_site_download(item_list):
    """Download sample material for make a fake site
    :param item_list: Download items form item_list
    :type item_list:list
    """
    try:
        if internet():
            for i in item_list:
                print("Downloading " + SAMPLE_DICT_MESSAGE[i] + " . . . [" + str(i + 1) + "/5]")
                print_line(70)
                urllib.request.urlretrieve(list(SAMPLE_DICT_ADDR.values())[i],
                                           os.path.join(IMAGE_DIR, list(SAMPLE_DICT_ADDR.keys())[i]))
            print("Done! All Material Downloaded")
            print_line(70)
        else:
            print("Error In Internet Connection!")
            print_line(70)
    except Exception as e:
        error_log(e)
        print("Error in downloading sample files check your internet conection")
        print_line(70)


def logger(status=False, perf_time=None):
    """Create the build log of the app
    :param status: show status of app.
    :param perf_time : show the time passed for generate files
    :type status:bool
    :type perf_time:float
    """
    if "log" not in os.listdir():
        os.mkdir("log")
    file = open(reduce(os.path.join, [os.getcwd(), "log", "build_log.txt"]), "a")
    if not status:
        file.write("Failed  " + str(datetime.datetime.now()) + "\n")
    else:
        file.write("Success " + str(datetime.datetime.now()) + "\n")
        file.write("Generation Time: " + str(perf_time) + "\n")
    file.close()


def error_log(msg):
    """Create the errorlog of the app

        :param msg: error message
        :type msg:str
    """
    if "log" not in os.listdir():
        os.mkdir("log")
    file = open(reduce(os.path.join, [os.getcwd(), "log", "error_log.txt"]), "a")
    file.write(str(datetime.datetime.now()) + " --> " + str(msg) + "\n")
    file.close()


def print_line(number, char="-"):
    """ Print a Line
    :param number: the amount char that in lien
    :param char  : the char that used to draw line
    :type number :int
    :type char : str
    >>> print_line(4)
    ----
    >>> print_line(5,"%")
    %%%%%
    """
    line = ""
    i = 0
    while (i < number):
        line += char
        i += 1
    print(line)


def name_standard(name):
    """ return the Standard VERSION of the input word
    :param name: the name that should be standard
    :type name:str
    :return name: the standard form of word as string
    >>> name_standard('test')
    'Test'
    >>> name_standard('TesT')
    'Test'
    """
    reponse_name = name[0].upper() + name[1:].lower()
    return reponse_name


def address_print():
    """
    Print the working directory
    :return:None
    """
    print_line(70, "*")
    print("Where --> " + SOURCE_DIR)
    print_line(70, "*")


def create_folder():
    """
    This Function Create Empty Folder At Begin
    :return:folder status as boolean
    """
    folder_flag = 0
    list_of_folders = os.listdir(SOURCE_DIR)
    for i in ["doc", "image", "output", "font"]:
        if i not in list_of_folders:
            os.mkdir(i)
            folder_flag += 1
            if i == "doc":
                file = open(os.path.join(DOC_DIR, "index.txt"), "w")
                if read_lorem() is None:
                    file.write("This is For First Page . . .")
                else:
                    file.write(read_lorem())
                file.close()
    return bool(folder_flag)


def page_name_update():
    """
    This Function Update Page Names
    :return: None
    """
    for i in os.listdir(DOC_DIR):
        if i.find(".txt") != -1 and i[:-4].upper() != "INDEX":
            ACTUAL_NAME.append(i[:-4])
            PAGE_NAME.append(i[:-4])


def menu_maker():
    """
    Top Menu Maker In each html page
    :return:site menu as string
    """
    result = "<center>"
    for i, item in enumerate(PAGE_NAME):
        if item == "Home":
            targets_blank = ""
        else:
            targets_blank = 'target="blank"'
            # Hyper Link To Each Page In HTML File
        result += '\t<a href="' \
                  + ACTUAL_NAME[i] + '.html"' + targets_blank + '>' + name_standard(item) + "</a>\n"
        result += "&nbsp\n"
    result += "</center>"
    result = result + "\t\t" + BREAK_LINE  # Add Break line to End Of The Menu
    return result  # Return All Of The Menu


def menu_writer():  #
    """
    Write menu_maker output in html and close file after
    :return:None
    """
    message = menu_maker()
    PAGE_NAME_length = len(PAGE_NAME)
    for i in range(PAGE_NAME_length):
        file = open(os.path.join(OUT_DIR, ACTUAL_NAME[i] + ".html"), "a")
        file.write(message)
        file.close()


def print_meta():
    """
    Add meta to html files
    :return static_meta: The meta that created
    """
    global meta_input
    meta_input = input("Please Enter Your Name : ")
    static_meta = '<meta name="description" content="Welcome to HOMEPAGE of ' + meta_input + '"/>\n'
    static_meta += '<meta property="og:title" content="' + meta_input + '"/>\n'
    static_meta += '<meta property="og:site_name" content="' + meta_input + '"/>\n'
    static_meta += '<meta property="og:image" content="favicon.ico" />\n'
    if len(meta_input) < 4:
        warnings.append("[Warning] Your input for name is too short!!")
    return static_meta


def html_init(name):
    """
    Create Initial Form Of each Html Page Like Title And HTML  And Body Tag.
    :param name: the name of html file.
    :type name:str
    """

    html_name = os.path.join(OUT_DIR, name + ".html")
    file = open(html_name, "w")
    file.write("<html>\n")
    file.write("\t<head>\n")
    if name == "index":
        file.write("\t\t<title>Welcome To My HOMEPAGE</title>\n")
    else:
        file.write("\t\t<title>" + name_standard(name) + "</title>\n")
    file.write('<link rel="stylesheet" href="styles.css" type="text/css"/>\n')
    css_link = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css'
    file.write('<link rel="stylesheet" href= ' + css_link + ' type="text/style"/>\n')

    if name == 'index':  # Add meta only for index page
        file.write(print_meta())

    file.write("\t</head>\n")
    file.write('\t<body class="body_tag">\n')
    file.close()


def html_end(name):
    """
    Create End Of The Html and close file
    :param name: The name of html file.
    :type name:str
    """
    html_name = os.path.join(OUT_DIR, name + ".html")
    file = open(html_name, "a")
    file.write("\t</body>\n")
    file.write("</html>")
    file.close()


def close_files():
    """
    Close all the files.
    :return:None
    """
    for i in files:
        if i.closed == False:
            i.close()


def LSM_translate(line, center):
    # TODO : write a document for this function
    """
    Convert size and style of each line in input plaintext
    :param line: the input line.
    :param center: flag of putting text in center
    :type center:bool
    :type line:str
    :return : return a list contain text,header_end and header_begin
    """
    line.strip()
    text = line
    header_start = '<h4 class="color_tag">'
    header_end = "</h4>"
    if line.find("[L]") != -1:
        header_start = '<h2 class="color_tag">'
        header_end = "</h2>"
        text = line[3:]
    elif line.find("[S]") != -1:
        header_start = '<h5 class="color_tag">'
        header_end = "</h5>"
        text = line[3:]
    elif line.find("[M]") != -1:
        text = line[3:]
    if center:  # Centuries Text If Condition Is True For Manual Centering
        header_start = "<center>" + header_start
        header_end += "</center>"
    if text.find("[center]") != -1:  # Find Center Tag In Each Line
        header_start = "<center>" + header_start
        header_end += "</center>"
        text = text[:text.find("[center]")]
    return [text, header_end, header_start]


def print_text(text_file, file, center=False, close=False):  # Write Text Part Of Each Page
    """Write the text part of each page

    :param text_file: Text that should be written.
    :param file     : The file that text will be written inside.
    :param center: flag of putting text in center
    :param close : flag of closing file after editing
    :type close : bool
    :type center: bool
    :type file:_io.TextIOWrapper
    :type text_file:str
    :return:None
    """

    text_code = ""
    for line in text_file:
        if len(line) == 1:
            text_code = SPACE
        else:
            text_header = LSM_translate(line, center)
            text = text_header[0]
            header_end = text_header[1]
            header_start = text_header[2]
            text_code = header_start + text + header_end + "\n"
        file.write(text_code)
    if close:
        file.close()


def print_image(file, image_format="jpg", close=False):
    """Write Image Part OF The Page.

    :param file: The file that images will be added.
    :param close : flag of closing file after editing
    :param image_format: the format of image
    :type close : bool
    :type image_format:str
    :type file:_io.TextIOWrapper
    :return:None
    """
    for i, item in enumerate(SIZE_BOX):
        print(i, "-", item)
    image_size = int(input("Please Enter Profile Image Size : "))  # Choose Profile Image Size
    image_size_string = SIZE_BOX[2]  # Getting Html String From SIZE_BOX list default mode (Medium)
    if 0 <= image_size < len(SIZE_BOX):
        image_size_string = SIZE_BOX[image_size]
    image_code = '<center><img src="image.' + image_format + '"' + ', width=' + image_size_string + ' alt="profile image"></img></center>\n'
    file.write(image_code)
    if close:
        file.close()


def print_download(file, name, link, center=False, close=False):
    """ Create Download Link in page

    :param file: The file that contain html of page.
    :param name: The name of the link
    :param link: The place that name is Linked
    :param center: put the text in center
    :param close : close file after done editing
    :type center: bool
    :type close : bool
    :type link:str
    :type name:str
    :type file:_io.TextIOWrapper
    :return:None
    """
    link_code = "<a href=" + '"' + link + '"' + TARGET_BLANK + '>' + name + "</a>"
    if center:
        link_code = "<center>" + link_code + "</center>"
    file.write(link_code + "\n")
    file.write(BREAK_LINE)
    if close:
        file.close()


def print_adv(file, close=True):
    """
    Print the advertisement (qpage footer)
    :param file  : The file that should adv to it.
    :param close : Close file after add
    :type file:_io.TextIOWrapper
    :type close:bool
    :return: None
    """
    file.write(BREAK_LINE)
    file.write(
        '<center>' + "<p>" + "Generated " + today_time + " By" + "</p>" + '<a href=' + '"' + HOMEPAGE + '"' + TARGET_BLANK + '>' + '<img src="' + create_badge(
            random=True) + '"alt="Qpage">' + '</a> </center>')
    if close:
        file.close()


def build_index(file):
    """
    Find and build index page
    :param file: The index file.
    :type file:_io.TextIOWrapper
    :return:None
    """
    image_name = ""
    img_format = "jpg"
    file_of_images = os.listdir(IMAGE_DIR)
    for i in file_of_images:
        for form in IMFORMAT_BOX:
            if i.find("." + form) != -1:
                image_name = os.path.join(IMAGE_DIR, i)
                img_format = form
                global IMAGE_COUNTER
                IMAGE_COUNTER = 1
                break
    shutil.copyfile(image_name, os.path.join(OUT_DIR, "image." + img_format))
    print_image(file, img_format)


def build_resume(file):
    """
    Find and build resume page.
    :param file: The resume file.
    :type file:_io.TextIOWrapper
    :return:None
    """
    resume_name = ""
    file_of_docs = os.listdir(DOC_DIR)
    for i in file_of_docs:
        if i.find(".pdf") != -1:
            resume_name = os.path.join(DOC_DIR, i)
            global PDF_COUNTER
            PDF_COUNTER = 1
            break
    shutil.copyfile(resume_name, os.path.join(OUT_DIR, "Resume.pdf"))
    print_download(file, "Download Full Version", "Resume.pdf", center=True)


def contain(name):
    """
    Main function that open each page HTML file and call other function to write data in it
    :param name: the name of the file that should be written
    :type name:str
    :return:None
    """
    #
    file = open(os.path.join(OUT_DIR, name + ".html"), "a")
    text_file = open(os.path.join(DOC_DIR, name + ".txt"), "r")
    files.append(file)
    files.append(text_file)

    if name.upper() == "INDEX":
        build_index(file)
    elif name.upper() == "RESUME":
        build_resume(file)

    print_text(text_file, file)
    if name.upper() == "INDEX":
        print_adv(file)


def clear_folder(path):
    """
    This function get path of folder and delete its contains
    :param path: the path that gonna be deleted.
    :type path:str
    :return: None
    """

    if os.path.exists(path):
        list_of_files = os.listdir(path)
        for file in list_of_files:
            os.remove(os.path.join(path, file))
    else:
        os.mkdir(path)


def print_warning():
    """
     Print warnings!
    :return:None
    """
    print(str(len(warnings)) + " Warning , 0 Error")
    show_items(warnings)


def get_color_code():
    """
    Ask for selecting color of text and background
    :return list: background and text color
    >>> get_color_code()
    0 - White
    1 - Black
    2 - Purple
    3 - Yellow
    4 - Orange
    5 - Green
    6 - Blue
    Please enter your background color : 1
    Please enter your text color : 2
    [1, 2]
    """
    for i, item in enumerate(COLOR_BOX):
        print(i, "-", item)
    back_color_code = int(input("Please enter your background color : "))
    if back_color_code not in range(7):
        back_color_code = 0
    text_color_code = int(input("Please enter your text color : "))
    if text_color_code not in range(7):
        text_color_code = 1
    return [back_color_code, text_color_code]


def color_code_map():
    """
    Check and insert colors that is chosen.
    :return list: background and text color
    """
    [back_color_code, text_color_code] = get_color_code()
    if text_color_code == back_color_code:
        warnings.append(WARNING_DICT["color_warning"] + " Your text color and background color are same!!")
    background_color = COLOR_BOX[back_color_code]  # convert code to color string in COLOR_BOX
    text_color = COLOR_BOX[text_color_code]  # convert code to color string in COLOR_BOX
    return [background_color, text_color]


def css_font(font_folder):
    """
     Search and file all fonts.
    :param font_folder: the folder to search.
    :type font_folder:list
    :return list : font_flag and the current format
    """
    font_flag = 0  # 0 If there is no font file in font_folder
    current_FONT_FORMAT = None
    for i in font_folder:
        for j in FONT_FORMAT:  # search for other font format in font box
            if i.lower().find(j) != -1:  # If there is a font in font folder
                shutil.copyfile(os.path.join(FONT_DIR, i),
                                os.path.join(OUT_DIR, "qpage" + j))  # copy font file to output folder
                font_flag = 1  # Turn Flag On
                current_FONT_FORMAT = j  # font format of current selected font for css editing
    return [font_flag, current_FONT_FORMAT]


def font_creator(css_file, font_section):
    """
     Ask and Select font.
    :param css_file: the file that font css will be added to.
    :param font_section: the font section of css file
    :type css_file:_io.TextIOWrapper
    :type font_section:str
    :return font_section: the font section of css after edit as string
    """
    font_folder = os.listdir(FONT_DIR)
    details = css_font(font_folder)
    current_FONT_FORMAT = details[1]
    font_flag = details[0]

    if font_flag == 1:  # check flag if it is 1
        css_file.write(
            "@font-face{\nfont-family:qpagefont;\nsrc:url(qpage"
            + current_FONT_FORMAT
            + ");\n}\n")  # Write font-face in html

        font_section = "font-family:qpagefont;\n"  # Update Font Section For Body Tag
        for i, item in enumerate(FONTSTYLE_BOX):
            print(i, "-", item)
        font_style = int(input(" Please choose your font style "))
        if font_style < len(FONTSTYLE_BOX):
            font_style = FONTSTYLE_BOX[font_style]
        else:
            font_style = "normal"
        font_section = font_section + "font-style:" + font_style + ";\n"
    else:
        warnings.append(WARNING_DICT["font_warning"] + " There is no specific font set for this website!!")
    return font_section


def css_creator():
    """
    Ask For background and text color in and make css base
    :return:None
     """
    font_section = 'font-family : Georgia , serif;\n'
    colors = color_code_map()
    background_color = colors[0]
    text_color = colors[1]

    css_file = open(os.path.join(OUT_DIR, "styles.css"), "w")  # open css file
    font_section = font_creator(css_file, font_section)

    css_file.write(
        ".body_tag{\n"
        + "background-color:"
        + background_color
        + ";\n"
        + font_section
        + CSS_MARGIN
        + CSS_ANIMATION_1
        + "}\n")  # write body tag

    css_file.write(".color_tag{\n" + "color:" + text_color + ";\n}")  # write color_tag in css
    css_file.write(CSS_ANIMATION_2)
    css_file.close()  # close css file


def preview():
    """
    Preview website in browser
    :return:None
     """
    # TODO: not working on unix

    webbrowser.open(os.path.join(OUT_DIR, "index.html"))


def error_finder():
    """
    Check and find error that display it
    :return : error and pass vector as list
    """
    error_vector = []
    pass_vector = []
    PDF_COUNTER = 0
    # image_list = os.listdir(IMAGE_DIR)
    doc_list = os.listdir(DOC_DIR)
    if IMAGE_COUNTER == 1:
        pass_vector.append("[Pass] Your profile image in OK!!")
    else:
        error_vector.append(ERROR_DICT["image_error"] + " Your profile image is not in correct format")
    if len(doc_list) == 0:
        error_vector.append(ERROR_DICT["empty_error"] + "There is no file in doc folder ( index.txt and .pdf file in "
                                                        "necessary)")
    else:
        if "index.txt" in doc_list:
            pass_vector.append("[Pass] index.txt file OK!")
        else:
            error_vector.append(ERROR_DICT["firstpage_error"] + " index.txt is not in doc folder!")
        if PDF_COUNTER == 0:
            error_vector.append(ERROR_DICT["resume_error"] + "[Error] Where Is Your Resume File? It should be in doc "
                                                             "folder")
        else:
            pass_vector.append("[Pass] Your Resume File is OK!!")
    return [error_vector, pass_vector]


def icon_creator():
    """
     Find .ico file and use it as favicon of website.
     :return:None
     """
    icon_flag = 0
    for file in os.listdir(IMAGE_DIR):
        if file.endswith('ico'):
            shutil.copy(os.path.join(IMAGE_DIR, file), OUT_DIR)
            os.rename(os.path.join(OUT_DIR, file), os.path.join(OUT_DIR, 'favicon.ico'))
            icon_flag = 1
            break
    if "favicon.ico" in os.listdir(SOURCE_DIR) and icon_flag == 0:
        shutil.copy(os.path.join(SOURCE_DIR, "favicon.ico"), OUT_DIR)
        warnings.append(WARNING_DICT["icon_warning"] + " There is no icon for this website")


def robot_maker():
    """
     Create Robots.txt for pages
     :return:None
    """
    robots = open(os.path.join(OUT_DIR, "robots.txt"), "w")
    robots.write("User-agent: *\n")
    robots.write("Disallow: ")
    robots.close()


def internet(host="8.8.8.8", port=53, timeout=3):
    """ Check Internet Connections.
    :param  host: the host that check connection to
    :param  port: port that check connection with
    :param  timeout: times that check the connnection
    :type host:str
    :type port:int
    :type timeout:int
    :return bool: True if Connection is Stable
    >>> internet() # if there is stable internet connection
    True
    >>> internet() # if there is no stable internet connection
    False
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as ex:
        error_log(ex)
        return False


def server():
    """
    Get Server response.
    :return:None
    >>> server()
    Installed Saved!
    """
    # global meta_input
    headers = {'content-type': 'application/json', "NAME": meta_input, "VERSION": VERSION, "SYSTEM": system_details(),
               "IP": find_global_ip()}
    response = requests.get(SERVER_API, headers=headers)
    if response.status_code == 200:
        print("Installed Saved!")


def version_control():
    """
     Check and update version status
     :return:None
    """

    try:
        # print("Check for new VERSION . . .")
        # print_line(70)
        VERSION_pattern = r"last_VERSION:(.+)"
        if internet():
            response = requests.get("http://www.qpage.ir/releases.html")
            body = response.text
            last_VERSION = float(re.findall(VERSION_pattern, body)[0][:-3])
            if last_VERSION > float(VERSION):
                print_line(70)
                print("**New VERSION Of Qpage Is Available Now (VERSION " + str(last_VERSION) + ")**")
                print("Download Link -->" + "https://github.com/sepandhaghighi/qpage/archive/v" + str(
                    last_VERSION) + ".zip")
                print_line(70)
            else:
                # TODO : fix VERSION control else
                pass
                # print("Already Updated!!!")
                # print_line(70)
    except Exception as e:
        error_log(e)
        pass


def enter_to_exit():
    """
    Quit Project by pressing a key.
    :return:None
    """

    print_line(70, "*")
    response = input("Enter [R] for restart Qpage and any other key to exit : ")
    if response.upper() != "R":
        sys.exit()


def wait_func(iteration=2):
    """
    Wait for-in range Iteration.
    :param iteration: the amount of wait.
    :type iteration:int
    :return:None
    >>> wait_func(4)
    .
    .
    .
    .
    >>> wait_func()
    .
    .
    """

    for _ in range(iteration):
        time.sleep(1)
        print(".")
if __name__=="__main__":
    doctest.testmod()
