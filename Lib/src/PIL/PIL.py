from os.path import dirname, join
import Image

sourceFile = join(dirname(__file__), 'source.jpg')
resizeFile = join(dirname(__file__), 'resize.jpg')
rotateFile = join(dirname(__file__), 'rotate.jpg')
cut_paste_File = join(dirname(__file__), 'cut_paste.jpg')

im = Image.open(sourceFile)

def resize(image, width, height):
    return image.resize((width, height))

def rotate(image, angle):
    return image.rotate(angle)  #Counterclockwise

def cut_paste(image, box):
    m = image.crop(box)
    m = m.transpose(Image.ROTATE_180)
    image.paste(m, box)
    return image

def getInfo(image):
    startw, starth, endw, endh = image.getbbox()
    print startw, starth, endw, endh

#resize(im, 800, 600).save(resizeFile)
#rotate(im, 45).save(rotateFile)
#cut_paste(im, (1000, 1000 ,2000, 2000)).save(cut_paste_File)
#getInfo(im)

