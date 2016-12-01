from qpage import *
import sys
def run_2():
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
    print("Homepage is ready")
    print("Upload output folder contains directly to your host")
    print("Please Don't Change HTML Files Name")
    print_warning()
    if internet():
        server()
    browse = int(input("Preview Homepage?[1] or Not[2]"))
    if browse == 1:
        preview()
        close_files()
def run(control_flag=True):
    try:
        response = create_folder()
        print("QPAGE By S.Haghighi & M.M.Rahimi")
        print("Version : " + version)
        if control_flag==True:
            version_control()
        if response:
            print(
                "At least one of the folders create for the first time ,\n"
                " please put your data in proper order and run program again\n Program Reboot Automaticly in 3 Sec")
            wait_func(3)
            run(False)
            sys.exit()
        clear_folder(out_dir)  # clear all of files in output directory
        page_name_update()  # update page names
        run_2()
    except FileNotFoundError:  # error exception in FileNotFound ( When Something Missed)
        close_files()
        vector_2 = error_finder()
        error_vector = vector_2[0]
        pass_vector = vector_2[1]
        print(str(len(error_vector)) + " Error")
        print("Please Check Following :\n")
        for i in range(len(error_vector)):
            print(str(i + 1) + "-" + error_vector[i])
        for i in range(len(pass_vector)):
            print(str(i + len(error_vector) + 1) + "-" + pass_vector[i])
        enter_to_exit()
    except ValueError:
        print("Bad Input")
        enter_to_exit()

if __name__ == "__main__":
    run()

