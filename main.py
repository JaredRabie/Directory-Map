import os

root_directory = "C:/Users/Jared Rabie/Root"
print(os.listdir(root_directory))

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

def explore_folder(path, depth = 0):
    try:
        lst = os.listdir(path)
    except NotADirectoryError:
        return ...
    lst.sort()
    for item in lst:
        print("\t"*depth, item, sep="")
        if "." not in item:
            explore_folder(path + "/{}/".format(item), depth+1)


root_directory = get_root_directory()
explore_folder(root_directory)
