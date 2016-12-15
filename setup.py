from qpage import *
import sys


def error_handler():
    close_files()  # Close all of the open files
    vector_2 = error_finder()  # load error and pass vector
    error_vector = vector_2[0]  # extract errors
    pass_vector = vector_2[1]  # extract pass
    print(str(len(error_vector)) + " Error")  # print  number of errors
    print("Please Check Following :\n")
    for i in range(len(error_vector)):  # print errors
        print(str(i + 1) + "-" + error_vector[i])  # print pass
    for i in range(len(pass_vector)):
        print(str(i + len(error_vector) + 1) + "-" + pass_vector[i])
    enter_to_exit()  # get input from user to continue
    main_handler()


def file_handler():
    for i in actual_name:
        html_init(i)  # create pages html files
    menu_writer()  # write menu for each html file
    for i in actual_name:
        contain(i)  # write contains of each page
        html_end(i)  # end tags of each page
    css_creator()  # create css file
    icon_creator()
    robot_maker()
    close_files()


def main_handler_2():
    file_handler()  # call file_handler
    print("Homepage is ready")
    print("Upload output folder contains directly to your host")
    print("Please Don't Change HTML Files Name")
    address_print()  # print files location
    print_warning()  # print all of the detected warnings
    logger(True)  # add success run of qpage to local logger
    if internet():  # check internet connection
        server()  # send query to qpage server
    browse = int(input("Preview Homepage?[1] or Not[2]"))  # get input from user for preview of site
    if browse == 1:  # check browse status
        preview()  # call preview function
        close_files()  # close all of the open files


def response_handler(response):
    if response:  # check reposne status
        print(
            "At least one of the folders create for the first time ,\n"
            " please put your data in proper order and run program again\n Program Reboot Automaticly in 3 Sec")
        wait_func(3)  # wait for 3 sec
        main_handler(False)  # call main_handler again with False version control flag
        sys.exit()  # exit program


def sample_handler():
    response = input(
        "Press [S] to enter sample site material runing or other keys to continue with your data")  # Get Input form user for loading sample files or continue
    print_line(70)  # print line
    if response.upper() == "S":  # check response status
        sample_site_download(is_sample_downloaded())  # Call sample download


def main_handler(control_flag=True):
    try:
        response = create_folder()  # Check Folder and Files Status
        print("QPAGE By S.Haghighi & M.M.Rahimi")
        print("Version : " + version)
        address_print()  # Print Files Location
        if control_flag == True:  # Check if version control passed in prev step
            version_control()  # Check for new version of qpage
        response_handler(response)  # call response_handler
        sample_handler()  # run sample handler
        clear_folder(out_dir)  # clear all of files in output directory
        page_name_update()  # update page names
        main_handler_2()  # call part_2 of main_handler
    except FileNotFoundError:  # error exception in FileNotFound ( When Something Missed)
        logger(False)  # Add Failed Run to local logger file
        error_handler()  # call error_handler
    except ValueError:
        print("Bad Input")
        logger(False)  # Add Failed Run to local logger file
        close_files()  # Close all of the opne files
        enter_to_exit()  # get input from user to continue
        main_handler()  # call part_1 of main_handler , restart from the first
    except PermissionError:
        logger(False)  # Add Failed Run to local logger file
        print("Files Is Open By Another Program")
        close_files()  # Close all of the opne files
        enter_to_exit()  # get input from user to continue
        main_handler()  # call part_1 of main_handler , resetart from the first


if __name__ == "__main__":
    main_handler()
