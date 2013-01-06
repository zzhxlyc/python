import glob
import os
import shutil

#can not do with non-anci char
for file in glob.glob('E:\Downloads\*.rmvb'):
    print file
    
#test file(if exist, can read, can write ...), see os.access()

#copy all the files in src directory into dest
print os.access('F:\Favourite', os.R_OK)
shutil.copyfile('F:\Favourite', 'E:\Temp')
