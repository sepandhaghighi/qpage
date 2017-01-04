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

meta_input = ""


def convert_bytes(num):
    """ convert num to idiomatic byte unit

    :param num: the input number.
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size():
    """ Print the size of output file

    """
    list_of_files = os.listdir(out_dir)
    response = 0
    for file in list_of_files:
        file_info = os.stat(os.path.join(out_dir, file))
        response += file_info.st_size
    print_line(70, "*")
    print("Used Space --> " + convert_bytes(response))
    print_line(70, "*")


def download_badge(address):
    """ Download badge for website

    :param address: the address that should get badge
    """
    r = requests.get(address, stream=True)
    with open(os.path.join(image_dir, "badge.svg"), 'wb') as f:
        shutil.copyfileobj(r.raw, f)


def random_badge_color():
    """return a random color for badge

    """
    random_index = random.randint(0, len(badge_color_list) - 1)
    return badge_color_list[random_index]


def system_details():
    """ Show detail of system that code is runnig on

    """
    return platform.node() + " , " + platform.processor() + " ,  " + platform.platform()


def generation_time(time_1=None):
    """ Calculate the generation time

    :param time_1: time that passed but not counted in generation time
    :return :the amount of time that passed .
    """
    if time_1 is None:
        return time.perf_counter()
    else:
        return time.perf_counter() - time_1


def find_global_ip():
    """ Find the ip for use in API

    :return: return the IP.
    """
    try:
        response = requests.get(ip_finder_api)
        return response.text[:-1]
    except:
        return "0.0.0.0"


def create_badge(subject="qpage", status=version, color="blue", random=False):
    if random:
        color = random_badge_color()
    else:
        if color not in badge_color_list:
            color = "orange"
    badge_adr = adv_badge_static + subject + "-" + status + "-" + color + '.svg'
    if internet():
        download_badge(badge_adr)
        return os.path.join(image_dir, "badge.svg")
    else:
        return badge_adr


def is_sample_downloaded():
    """ Check the sample site material is downloaded

    :return : list of the materials
    """
    download_list = []
    if "profile.png" not in os.listdir(image_dir):
        download_list.append(0)
    if "font.TTF" not in os.listdir(font_dir):
        download_list.append(1)
    if "resume.pdf" not in os.listdir(doc_dir) and "resume.txt" not in os.listdir(doc_dir):
        download_list.extend([2, 3])
    if "icon.ico" not in os.listdir(image_dir):
        download_list.append(4)
    return download_list


def download_lorem():
    """ Download the lorem file

    """
    if internet():
        urllib.request.urlretrieve("http://www.qpage.ir/sample/Latin-Lipsum.txt", "Latin-Lipsum.txt")
    else:
        print("Error In Download Lorem")


def read_lorem(char=100):
    """ find and read lorem

    :param char: the amount of char that needed
    :return : the lorme string
    """
    try:
        if "Latin-Lipsum.txt" not in os.listdir(work_dir):
            download_lorem()
        lorem_file = open("Latin-Lipsum.txt", "r")
        lorem_text = lorem_file.read()
        lorem_file.close()
        return " ".join(lorem_text.split(" ")[:char])
    except:
        return None


def sample_site_download(item_list):
    """Download sample material for make a fake site

    :param item_list: Download items form item_list
    """
    try:
        if internet():
            for i in item_list:
                print("Downloading " + sample_dict_message[i] + " . . . [" + str(i + 1) + "/5]")
                print_line(70)
                urllib.request.urlretrieve(list(sample_dict_addr.values())[i],
                                           os.path.join(image_dir, list(sample_dict_addr.keys())[i]))
            print("Done! All Material Downloaded")
            print_line(70)
        else:
            print("Error In Internet Connection!")
            print_line(70)
    except:
        print("Error in downloading sample files check your internet conection")
        print_line(70)


def logger(status=False, perf_time=None):
    """Show the log of the app

    :param status: show status of app.
    :param perf_time : show the time passed for generate files
    """
    file = open("build_log.txt", "a")
    if not status:
        file.write("Failed  " + str(datetime.datetime.now()) + "\n")
    else:
        file.write("Success " + str(datetime.datetime.now()) + "\n")
        file.write("Generation Time: " + str(perf_time) + "\n")
    file.close()


def print_line(number, char="-"):
    """ Print a Line

    :param number: the amount char that in lien
    :param char  : the char that used to draw line
    """
    line = ""
    for i in range(number):
        line += char
    print(line)


def name_standard(name):
    """ return the Standard version of the input word

    :param name: the name that should be standard
    :return name: the standard form of word
    """
    reponse_name = name[0].upper() + name[1:].lower()
    return reponse_name


def address_print():
    """Print the working directory

    """
    print_line(70, "*")
    print("Where --> " + work_dir)
    print_line(70, "*")


def create_folder():
    """This Function Create Empty Folder At Begin

    """
    folder_flag = 0
    list_of_folders = os.listdir(work_dir)
    for i in ["doc", "image", "output", "font"]:
        if i not in list_of_folders:
            os.mkdir(i)
            folder_flag += 1
            if i == "doc":
                file = open(os.path.join(doc_dir, "index.txt"), "w")
                if read_lorem() is None:
                    file.write("This is For First Page . . .")
                else:
                    file.write(read_lorem())
                file.close()
    return bool(folder_flag)


def page_name_update():
    """This Function Update Page Names

    """
    for i in os.listdir(doc_dir):
        if i.find(".txt") != -1 and i[:-4].upper() != "INDEX":
            actual_name.append(i[:-4])
            page_name.append(i[:-4])


def menu_maker():
    """Top Menu Maker In each html page

    """
    result = "<center>"
    for i,item in enumerate(page_name):
        if item == "Home":
            targets_blank = ""
        else:
            targets_blank = 'target="blank"'
            # Hyper Link To Each Page In HTML File
        result += '\t<a href="' \
                    + actual_name[i] + '.html"' + targets_blank + '>' + name_standard(item) + "</a>\n"
        result += "&nbsp\n"
    result += "</center>"
    result = result + "\t\t" + break_line  # Add Break line to End Of The Menu
    return result  # Return All Of The Menu


def menu_writer():  #
    """Write menu_maker output in html and close file after

    """
    message = menu_maker()
    for i,item in enumerate(page_name):
        file = open(os.path.join(out_dir, actual_name[i] + ".html"), "a")
        file.write(message)
        file.close()


def print_meta():
    """Add meta to html files

    :return static_meta: The meta that created
    """
    global meta_input
    meta_input = input("Please Enter Your Name : ")
    static_meta = '<meta name="description" content="Welcome to homepage of ' + meta_input + '"/>\n'
    static_meta += '<meta property="og:title" content="' + meta_input + '"/>\n'
    static_meta += '<meta property="og:site_name" content="' + meta_input + '"/>\n'
    static_meta += '<meta property="og:image" content="favicon.ico" />\n'
    if len(meta_input) < 4:
        warnings.append("[Warning] Your input for name is too short!!")
    return static_meta


def html_init(name):
    """Create Initial Form Of each Html Page Like Title And HTML  And Body Tag.

    :param name: the name of html file.
    """

    html_name = os.path.join(out_dir, name + ".html")
    file = open(html_name, "w")
    file.write("<html>\n")
    file.write("\t<head>\n")
    if name == "index":
        file.write("\t\t<title>Welcome To My Homepage</title>\n")
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
    """Create End Of The Html and close file

    :param name: The name of html file.
    """
    html_name = os.path.join(out_dir, name + ".html")
    file = open(html_name, "a")
    file.write("\t</body>\n")
    file.write("</html>")
    file.close()


def close_files():
    """Close all the files.

    """
    for i in files:
        i.close()


def LSM_translate(line, center):
    # TODO : write a document for this function
    """ ????

    :param line: the input line.
    :param center: put it in center

    :return : return a list contain text header end and header begin
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

    :param text_file: Text tha should be written.
    :param file     : The file that text will be written inside.
    :param center   : put the text in center.
    :param close    : close file after done editing

    :type close : bool
    :type center: bool

    """

    text_code = ""
    for line in text_file:
        if len(line) == 1:
            text_code = space
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
    :param close : close file after done editing.
    :param image_format: the format of image

    :type close : bool
    """
    for i,item in enumerate(size_box):
        print(i, "-", item)
    image_size = int(input("Please Enter Profile Image Size : "))  # Choose Profile Image Size
    image_size_string = size_box[2]  # Getting Html String From size_box list default mode (Medium)
    if 0 <= image_size < len(size_box):
        image_size_string = size_box[image_size]
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

    """
    link_code = "<a href=" + '"' + link + '"' + target_blank + '>' + name + "</a>"
    if center:
        link_code = "<center>" + link_code + "</center>"
    file.write(link_code + "\n")
    file.write(break_line)
    if close:
        file.close()


def print_adv(file, close=True):
    """ Print the advertisement.

    :param file  : The file that should ad to it.
    :param close : Close file after add ad
    """
    file.write(break_line)
    file.write(
        '<center>' + "<p>" + "Generated " + today_time + " By" + "</p>" + '<a href=' + '"' + homepage + '"' + target_blank + '>' + '<img src="' + create_badge(
            random=True) + '"alt="Qpage">' + '</a> </center>')
    if close:
        file.close()


def build_index(file):
    """ Find and build index page

    :param file: The index file.
    """
    image_name = ""
    img_format = "jpg"
    file_of_images = os.listdir(image_dir)
    for i in file_of_images:
        for form in imformat_box:
            if i.find("." + form) != -1:
                image_name = os.path.join(image_dir, i)
                img_format = form
                global image_counter
                image_counter = 1
                break
    shutil.copyfile(image_name, os.path.join(out_dir, "image." + img_format))
    print_image(file, img_format)


def build_resume(file):
    """ Find and build resume page.

    :param file: The resume file.
    """
    resume_name = ""
    file_of_docs = os.listdir(doc_dir)
    for i in file_of_docs:
        if i.find(".pdf") != -1:
            resume_name = os.path.join(doc_dir, i)
            global pdf_counter
            pdf_counter = 1
            break
    shutil.copyfile(resume_name, os.path.join(out_dir, "Resume.pdf"))
    print_download(file, "Download Full Version", "Resume.pdf", center=True)


def contain(name):
    """main function That Open Each Page HTML File and call other function to write data in it

    :param name: the name of the file that should be written
    """
    #
    file = open(os.path.join(out_dir, name + ".html"), "a")
    text_file = open(os.path.join(doc_dir, name + ".txt"), "r")
    files.append(file)
    files.append(text_file)

    if name.upper() == "INDEX":
        build_index(file)
    elif name.upper() == "RESUME":
        build_resume(file)

    print_text(text_file, file)
    print_adv(file)


def clear_folder(path):
    """This Function Get Path Of Foldr And Delete Its Contains

    :param path: the path that gonna be deleted.
    """

    if os.path.exists(path):
        list_of_files = os.listdir(path)
        for file in list_of_files:
            os.remove(os.path.join(path, file))
    else:
        os.mkdir(path)


def print_warning():
    """ Print Warinigns!

    """
    print(str(len(warnings)) + " Warning , 0 Error")
    for i,item in enumerate(warnings):
        print(str(i + 1) + "-" + item)


def get_color_code():
    """Ask for selecting color of text and background

    :return list: background and text color
    """
    for i,item in enumerate(color_box):
        print(i, "-", item)
    back_color_code = int(input("Please enter your background color : "))
    if back_color_code not in range(7):
        back_color_code = 0
    text_color_code = int(input("Please enter your text color : "))
    if text_color_code not in range(7):
        text_color_code = 1
    return [back_color_code, text_color_code]


def color_code_map():
    """ Check and insert colors that is chosen.

    :return list: background and text color
    """
    [back_color_code, text_color_code] = get_color_code()
    if text_color_code == back_color_code:
        warnings.append(warning_dict["color_warning"] + " Your text color and background color are same!!")
    background_color = color_box[back_color_code]  # convert code to color string in color_box
    text_color = color_box[text_color_code]  # convert code to color string in color_box
    return [background_color, text_color]


def css_font(font_folder):
    """ Search and file all fonts.

    :param font_folder: the folder to search.
    :return list : font_flag and the current format
    """
    font_flag = 0  # 0 If there is no font file in font_folder
    current_font_format = None
    for i in font_folder:
        for j in font_format:  # search for other font format in font box
            if i.lower().find(j) != -1:  # If there is a font in font folder
                shutil.copyfile(os.path.join(font_dir, i),
                                os.path.join(out_dir, "qpage" + j))  # copy font file to output folder
                font_flag = 1  # Turn Flag On
                current_font_format = j  # font format of current selected font for css editing
    return [font_flag, current_font_format]


def font_creator(css_file, font_section):
    """ Ask and Select font.

    :param css_file: the file that font css will be added to.
    :param font_section: the font section of css file

    :return font_section: the font section of css after edit
    """
    font_folder = os.listdir(font_dir)
    details = css_font(font_folder)
    current_font_format = details[1]
    font_flag = details[0]

    if font_flag == 1:  # check flag if it is 1
        css_file.write(
            "@font-face{\nfont-family:qpagefont;\nsrc:url(qpage"
            + current_font_format
            + ");\n}\n")  # Write font-face in html

        font_section = "font-family:qpagefont;\n"  # Update Font Section For Body Tag
        for i,item in enumerate(fontstyle_box):
            print(i, "-", item)
        font_style = int(input(" Please choose your font style "))
        if font_style < len(fontstyle_box):
            font_style = fontstyle_box[font_style]
        else:
            font_style = "normal"
        font_section = font_section + "font-style:" + font_style + ";\n"
    else:
        warnings.append(warning_dict["font_warning"] + " There is no specific font set for this website!!")
    return font_section


def css_creator():
    """Ask For background and text color in and make css """
    font_section = 'font-family : Georgia , serif;\n'
    colors = color_code_map()
    background_color = colors[0]
    text_color = colors[1]

    css_file = open(os.path.join(out_dir, "styles.css"), "w")  # open css file
    font_section = font_creator(css_file, font_section)

    css_file.write(
        ".body_tag{\n"
        + "background-color:"
        + background_color
        + ";\n"
        + font_section
        + css_margin
        + css_animation_1
        + "}\n")  # write body tag

    css_file.write(".color_tag{\n" + "color:" + text_color + ";\n}")  # write color_tag in css
    css_file.write(css_animation_2)
    css_file.close()  # close css file


def preview():
    """Preview website in browser """
    # TODO: not working on unix

    webbrowser.open(os.path.join(out_dir, "index.html"))


def error_finder():
    """ Check and find error that display it"""
    error_vector = []
    pass_vector = []
    pdf_counter = 0
    image_list = os.listdir(image_dir)
    doc_list = os.listdir(doc_dir)
    if image_counter == 1:
        pass_vector.append("[Pass] Your profile image in OK!!")
    else:
        error_vector.append(error_dict["image_error"] + " Your profile image is not in correct format")
    if len(doc_list) == 0:
        error_vector.append(error_dict["empty_error"] + "There is no file in doc folder ( index.txt and .pdf file in "
                                                        "necessary)")
    else:
        if "index.txt" in doc_list:
            pass_vector.append("[Pass] index.txt file OK!")
        else:
            error_vector.append(error_dict["firstpage_error"] + " index.txt is not in doc folder!")
        if pdf_counter == 0:
            error_vector.append(error_dict["resume_error"] + "[Error] Where Is Your Resume File? It should be in doc "
                                                             "folder")
        else:
            pass_vector.append("[Pass] Your Resume File is OK!!")
    return [error_vector, pass_vector]


def icon_creator():
    """ Find .ico file and use it as favicon of website."""
    icon_flag = 0
    for file in os.listdir(image_dir):
        if file.endswith('ico'):
            shutil.copy(os.path.join(image_dir, file), out_dir)
            os.rename(os.path.join(out_dir, file), os.path.join(out_dir, 'favicon.ico'))
            icon_flag = 1
            break
    if "favicon.ico" in os.listdir(work_dir) and icon_flag == 0:
        shutil.copy(os.path.join(work_dir, "favicon.ico"), out_dir)
        warnings.append(warning_dict["icon_warning"] + " There is no icon for this website")


def robot_maker():
    """ Create Robots.txt for pages """
    robots = open(os.path.join(out_dir, "robots.txt"), "w")
    robots.write("User-agent: *\n")
    robots.write("Disallow: ")
    robots.close()


def internet(host="8.8.8.8", port=53, timeout=3):
    """ Check Internet Connections.

    :param  host: the host that check connection to
    :param  port: port that check connection with
    :param  timeout: times that check the connnection

    :return bool: True if Connection is Stable
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as ex:
        return False


def server():
    """Get Server response."""
    global meta_input
    headers = {'content-type': 'application/json', "NAME": meta_input, "Version": version, "SYSTEM": system_details(),
               "IP": find_global_ip()}
    response = requests.get(server_api, headers=headers)
    # print(response)
    # TODO : use the server response


def version_control():
    """ Check and update Versions. """

    try:
        # print("Check for new version . . .")
        # print_line(70)
        version_pattern = r"last_version:(.+)"
        if internet():
            response = requests.get("http://www.qpage.ir/releases.html")
            body = response.text
            last_version = float(re.findall(version_pattern, body)[0][:-3])
            if last_version > float(version):
                print_line(70)
                print("**New Version Of Qpage Is Available Now (Version " + str(last_version) + ")**")
                print("Download Link -->" + "https://github.com/sepandhaghighi/qpage/archive/v" + str(
                    last_version) + ".zip")
                print_line(70)
            else:
                # TODO : fix version control else
                pass
                # print("Already Updated!!!")
                # print_line(70)
    except:
        pass


def enter_to_exit():
    """Quit Project by pressing a key.

    """

    print_line(70, "*")
    response = input("Enter [R] for restart Qpage and any other key to exit : ")
    if response.upper() != "R":
        sys.exit()


def wait_func(iteration):
    """Wait for-in range Iteration.

    :param iteration: the amount of wait.
    """

    for _ in range(iteration):
        time.sleep(1)
        print(".")
