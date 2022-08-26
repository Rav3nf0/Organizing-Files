import zipfile, os

def backuptoZip(folder):
    folder =os.path.abspath(folder)

    number=1
    while True:
        zipfilename =os.path.basename(folder+ '-' +str(number) + '-'+'.zip')
        if not os.path.exists(zipfilename):

            break
        number =number +1
    print(f'Creating {zipfilename}...')
    backupZip =zipfile.ZipFile(zipfilename, 'w')

    for foldername,subfolders,filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        backupZip.write(foldername)
        
        for filename in filenames:
            newbase =os.path.basename(folder) +'_'
            if filename.startswith(newbase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername,filename))
    backupZip.close()
    print('done.')

backuptoZip('C:\\delicious')