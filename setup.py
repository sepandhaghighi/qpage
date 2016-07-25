from qpage import *
import webbrowser

if __name__ == "__main__":
    try:
        print("QPAGE By Sepand Haghighi")
        print("Version : " + version)
        clear_folder(out_dir)  # clear all of files in output directory
        page_name_update()  # update page names
        for i in actual_name:
            html_init(i)  # create pages html files
        menu_writer()  # write menu for each html file

        for i in actual_name:
            contain(i)  # write contains of each page
            html_end(i)  # end tags of each page
        css_creator()  # create css file
        print("Homepage is ready")
        print("Upload output folder contains directly to your host")
        print("Please Dont Change HTML Files Name")
        browse = int(input("Preview Homepage?[1] or Not[2]"))
        if browse == 1:
            preview()

    except FileNotFoundError:  # error exception in FileNotFound ( When Something Missed)
        print("Some File Missed!!")
        print(
            "Please Check Following :\n 1.Where Is Your Resume File? It should be in doc folder  \n 2.Where is your profile image file? it should be in image folder")
        print(" 3.Where is each page description text file? They Should be in doc folder ")
        input("")
    except ValueError:
        print("Bad Input")
        input("")
