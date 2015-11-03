from qpage import *  
if __name__=="__main__":
        try:
            clear_folder(out_dir)
            for i in actual_name:
                html_init(i)
            menu_writer()
    
            for i in actual_name:
                contain(i)
                html_end(i)
            css_creator()
            print("Homepage is ready")
            print("Upload output folder contains directly to your host")
            print("Please Dont Change HTML Files Name")
            input("")
        except FileNotFoundError: # error exception in FileNotFound ( When Something Missed)
            print ("Some File Missed!!")
            print ("Please Check Following :\n 1.Where Is Your Resume File? It should be in doc folder  \n 2.Where is your profile image file? it should be in image folder")
            print (" 3.Where is each page description text file? They Should be in doc folder ")
            input("")
            

    
    

