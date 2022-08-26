# Selective Copy
# Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg).
# Copy these files from whatever location they are in to a new folder.


import os, shutil

def selectcopy(folder,ext,dest):
    folder = os.path.abspath(folder)
    dest =os.path.abspath(dest)
    
    print('looking in',folder, 'for filenames with', ',' .join(ext) ,' extensions')
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            name, exten=os.path.splitext(filename)
            print('extension found :',exten)
            if exten in ext:
                print('copying', filename,'to',dest)
                shutil.copy(os.path.join(foldername, filename) ,dest)

ext=['.jpg ' , '.pdf']
folder='your_source_folder'
dest='your_dest_folder'
selectcopy(folder, ext,dest)
