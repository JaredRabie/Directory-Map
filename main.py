import os

root_directory = "C:/Users/Jared Rabie/Root"
print(os.listdir(root_directory))

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


explore_folder(root_directory)
