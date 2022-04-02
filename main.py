import os

def get_save_name(invalid = 0):
    if invalid == 0:
        save_name = input("Please enter save file name (Leave blank to prevent saving): ")
    else:
        save_name = input("Invalid directory! Try again: ")
    
    if save_name == "":
        return None
    try:
        save_file = open(save_name, "w")
        save_file.close()
    except:
        print("Error! Please try again.")
        get_save_name(1)
    
    return save_name

def get_root_directory(invalid = 0):
    if invalid == 0:
        dir = input("Please input a root directory: ")
    else:
        dir = input("Invalid directory! Try again: ")

    try:
        os.listdir(root_directory)
    except NotADirectoryError:
        get_root_directory(1)
    except:
        print("Unknown Error")
    return dir

def explore_folder(root_directory, depth = 0):
    
    try:
        lst = os.listdir(root_directory)
    except NotADirectoryError:
        return ...
    lst.sort()

    for item in lst:
        if save_name != None:
            save_file.write("\t"*depth+item+"\n")
        print("\t"*depth, item, sep="")
        if "." not in item:
            explore_folder(root_directory + "/{}/".format(item), depth+1)



save_name = get_save_name()
if save_name != None:
    save_file = open(save_name, 'w')
    
root_directory = get_root_directory()
explore_folder(root_directory)
save_file.close()