# Deleting Unneeded Files
# Write a program that walks through a folder tree and searches for exceptionally large files or folders—say, ones that have a file size of more than 100MB.
# (Remember that to get a file’s size, you can use os.path.getsize() from the os module.) Print these files with their absolute path to the screen.


import os,shutil

def findlarge(folder):
    size = 104857600 
    folder=os.path.abspath(folder)
    print('Finding large file in',folder,'for size over',size ,'bytes')

    var=False
    for foldername, subfolders,filenames in os.walk(folder):
        for filename in filenames:
           
            if os.path.getsize(filename)>size:
                var= True
                print('The file greater than 100MB :',filename)
    if var==False:
        print("\n no file found")

folder ="yourchoice"
findlarge(folder)
