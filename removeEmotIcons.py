from os import walk
from os import rename
from os import replace

folder_path = r"/home/zsolt/Desktop/GitHub/individual-scripts/testData/removeEmojiCopy2 (8th copy)" #input("Please enter the folder name where the files can be found that should be renamed:\t ")

for root, dir, folder in walk(folder_path):
    for file_name in folder:
        path_old_name = folder_path + r"/" + file_name
        emoji_list = ("🦑", "👍", "🔥", "🤷", "🤩", "♂️")
        for emoji_list_elem in emoji_list:
            if emoji_list_elem in file_name: 
                file_name = file_name.replace(emoji_list_elem, "")
                #print("new_name: ", new_name)

        path_new_name = folder_path + r"/" + file_name
        print("path_new_name: ", path_new_name)
        
        try:
            rename(path_old_name, path_new_name)
            print("File was renamed to: {} \n =================================".format(file_name))
        except Exception as e:
            print(e)

        
        
        
        
