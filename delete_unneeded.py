import os,shutil

def findlarge(folder):
    size = 104857600 
    folder=os.path.abspath(folder)
    print('Finding large file in',folder,'for size over',size ,'bytes')

    var=False
    for foldername, subfolders,filenames in os.walk(folder):
        for filename in filenames:
            #fileabspath=folder +os.path
            if os.path.getsize(filename)>size:
                var= True
                print('The file greater than 100MB :',filename)
    if var==False:
        print("\n no file found")

folder ="yourchoice"
findlarge(folder)