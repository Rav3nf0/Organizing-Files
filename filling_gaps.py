# Filling in the Gaps
# Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single folder and locates any gaps in the
# numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt).
# Have the program rename all the later files to close this gap.


import re,os,shutil

def fillgaps(folder,prefix):
    regex=re.compile(r'(.*?)(\d{3})(\.txt)')

    folder=os.path.abspath(folder)
    print(folder)
    FileNames=[]
    for filename in os.listdir(folder):
        if re.search(regex,filename):
            FileNames.append(filename)
#group(1)
#to sort the filenames appended
    
    print(FileNames)
    for i in range(len(FileNames)):
        var=re.search(regex,FileNames[i])
        #print(var.group(2))

        if int(var.group(2))==i+1:
            continue
        if i+1<10:
            
            newfile_name=prefix +'00'+str(i+1)+'.txt'
            print(newfile_name)
            oldname = os.path.join(folder, filename)
            newfile_name = os.path.join(folder, newfile_name)
            shutil.move(oldname, newfile_name)

        elif i+1<100:
            newfile_name=prefix +'0'+str(i+1)+'.txt'
            oldname = os.path.join(folder, filename)
            newfile_name = os.path.join(folder, newfile_name)
            shutil.move(oldname, newfile_name)
        else:
            newfile_name=prefix + str(i+1) + '.txt'
            oldname = os.path.join(folder, filename)
            newfile_name = os.path.join(folder, newfile_name)
            shutil.move(oldname, newfile_name)
    
folder =' YourChoice '
prefix ='spam'
fillgaps(folder,prefix)
