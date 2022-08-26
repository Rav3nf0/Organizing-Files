# Renaming Files with American-Style Dates to European-Style Dates

# This is what we do in the program:

# Create a regex that can identify the text pattern of American-style dates.
# Call os.listdir() to find all the files in the working directory.
# Loop over each filename, using the regex to check whether it has a date.
# If it has a date, rename the file with shutil.move().


import shutil,os,re
datePattern=re.complie(r"""^(.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20)\d\d)
(.*?)$
""",re.VERBOSE) #VERBOSE will allow whitespace and comments in the regex string to make it more readable.

for amerFilename in os.listdir('.'): #loop over the list of filenames returned from os.listdir()
    mo=datePattern.search(amerFilename)
    if mo == None:
        continue

textpart=mo.group(1)
monthpart=mo.group(2)
daypart=mo.group(4)
yearpart=mo.group(6)
extension=mo.group(8)

eurofilename = textpart+daypart+'-'+monthpart+'-'+yearpart+extension
absworkingdir = os.path.abspath('.')
amerFilename=os.path.join(absworkingdir,amerFilename)
eurofilename=os.path.join(absworkingdir,eurofilename)

print(f'renaming "{amerFilename}" to "{eurofilename}"...')
