from os import listdir, mkdir
from os.path import join, isdir, isfile
import Image

from timer import Timer

def resizeImage(image, width):
    w, h = image.getbbox()[2:]
    height = int(float(width) / w * h)
    return image.resize((width, height))

path = raw_input('Input the photo path:')
tempDir = join(path, 'Temp')

if not isdir(tempDir):
    mkdir(tempDir)

timer = Timer()
timer.begin()

list = listdir(path)
num = len(list) - 1
done = 0
print 'all is %s files' % (num)
for item in listdir(path):
    imagePath = join(path, item)
    newPath = join(tempDir, item)
    if isfile(imagePath):
        im = Image.open(imagePath)
        resizeImage(im, 800).save(newPath)
        done += 1
        print '%s is done, left %s...' % (newPath, num - done)
timer.end()
print timer.getTimeString()
avg = timer.getTime() / num
print '%s average for each' % (avg)

    
    
    