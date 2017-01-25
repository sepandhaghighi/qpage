from qpage import *
import sys
import gc


def error_handler():
    """
    Close files and check errors and start again main
    :return:None
        call:
        -close_files
        -error_finder
        -Show_items
        -enter_to_exit
        -main_handler
    """
    close_files()  # Close all of the open files
    vector_2 = error_finder()  # load error and pass vector
    error_vector = vector_2[0]  # extract errors
    pass_vector = vector_2[1]  # extract pass
    print(str(len(error_vector)) + " Error")  # print  number of errors
    print("Please Check Following :\n")
    show_items(error_vector)  # print error
    for i, item in enumerate(pass_vector):
        print(str(i + len(error_vector) + 1) + "-" + item)
    enter_to_exit()  # get input from user to continue
    main_handler()


def file_handler():
    """
    Write files
    :return:None
        call:
        -html_init
        -contain
        -css_creator
        -icon_creator
        -robot_maker
        -close_files
    """
    for i in ACTUAL_NAME:
        html_init(i)  # create pages html files
    menu_writer()  # write menu for each html file
    for i in ACTUAL_NAME:
        contain(i)  # write contains of each page
        html_end(i)  # end tags of each page
    css_creator()  # create css file
    icon_creator()
    robot_maker()
    close_files()


def main_handler_2(time_1=0):
    """
    Second part of main handler
    :param time_1: time that passed but not counted in generation time
    :type time_1:float
    :return:None
    call:
        -file_handler
        -address_print
        -print_warning
        -file_size
        -internet
        -server
        -preview
        -close_files
    """
    file_handler()  # call file_handler
    total_perf_time = generation_time(time_1)
    print("HOMEPAGE is ready,generated in " + str(total_perf_time) + " sec")
    print("Upload output folder contains directly to your host")
    print("Please Don't Change HTML Files Name")
    address_print()  # print files location
    print_warning()  # print all of the detected warnings
    file_size()
    logger(True, perf_time=total_perf_time)  # add success run of qpage to local logger
    if internet():  # check internet connection
        server()  # send query to qpage server
    browse = int(input("Preview HOMEPAGE?[1] or Not[2]"))  # get input from user for preview of site
    if browse == 1:  # check browse status
        preview()  # call preview function
        close_files()  # close all of the open files
    gc.collect()


def response_handler(response):
    """
    Calculate the generation time
    :param response: response flag , if there was a response run main handler again
    :type response:bool
    :return:None
    call:
        -wait_func
        -main_handler
    """
    if response:  # check response status
        print(
            "At least one of the folders create for the first time ,\n"
            " please put your data in proper order and run program again\n Program Reboot Automatically in 3 Sec")
        wait_func(3)  # wait for 3 sec
        main_handler(False)  # call main_handler again with False VERSION control flag
        sys.exit()  # exit program


def sample_handler():
    """
    Ask for run sample website
    :return:None
        call:
        -sample_site_download
        -is_sample_downloaded
    """
    # Get Input form user for loading sample files or continue
    response = input(
        "Press [S] to enter sample site material running or other keys to continue with your data")
    print_line(70)  # print line
    if response.upper() == "S":  # check response status
        sample_site_download(is_sample_downloaded())  # Call sample download


def main_handler(control_flag=True):
    """
    Main Handler
    :param control_flag: Check if VERSION control passed in prev step then Check for new VERSION of qpage
    :type control_flag:bool
    :return:None
        call:
        -generation_time
        -create_folder
        -print_logo
        -address_print
        -version_control
        -sample_handler
        -response_handler
        -page_name_update
        -main_handler_2
        -error_log
        -logger
        -close_files
        -enter_to_exit


    """
    try:
        start_time = generation_time()
        response = create_folder()  # Check Folder and Files Status
        print("QPAGE By S.Haghighi & M.M.Rahimi")
        print("VERSION : " + VERSION)
        print_logo()
        address_print()  # Print Files Location
        if control_flag:  # Check if VERSION control passed in prev step
            version_control()  # Check for new VERSION of qpage
        response_handler(response)  # call response_handler
        sample_handler()  # run sample handler
        clear_folder(OUT_DIR)  # clear all of files in output directory
        page_name_update()  # update page names
        main_handler_2(time_1=start_time)  # call part_2 of main_handler
    except FileNotFoundError as e:  # error exception in FileNotFound ( When Something Missed)
        error_log(e)
        logger(False)  # Add Failed Run to local logger file
        error_handler()  # call error_handler
    except ValueError as e:
        error_log(e)
        print("Bad Input")
        logger(False)  # Add Failed Run to local logger file
        close_files()  # Close all of the opne files
        enter_to_exit()  # get input from user to continue
        main_handler()  # call part_1 of main_handler , restart from the first
    except PermissionError as e:
        error_log(e)
        logger(False)  # Add Failed Run to local logger file
        print("Files Is Open By Another Program")
        close_files()  # Close all of the open files
        enter_to_exit()  # get input from user to continue
        main_handler()  # call part_1 of main_handler , resetart from the first


if __name__ == "__main__":
    main_handler()
