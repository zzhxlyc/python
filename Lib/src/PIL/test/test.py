import Image

def getInfo(image):
    startw, starth, endw, endh = image.getbbox()
    return endw - startw, endh - starth

def byPaste(image):
    img = Image.open('gbuzz.ico','r') 
    image.paste(img, (16,0))
    
    img = Image.open('gmark.ico','r') 
    image.paste(img, (0,0))
    image.save(file('out.jpg','w'))
    
def byPixel(image):
    img = Image.open('twitter.ico','r') 
    i = 0
    while i < 16:
        j = 0
        while j < 16:
            r, g, b = img.getpixel((i, j))
            if r == 0 and g == 0 and b == 0:
                r = g = b = 255
            image.putpixel((i, j), (r, g, b))
            j += 1
        i += 1
    
    img = Image.open('gmark.ico','r') 
    i = 16
    while i < 32:
        j = 0
        while j < 16:
            r, g, b = img.getpixel((i - 16, j))
            if r == 0 and g == 0 and b == 0:
                r = g = b = 255
            image.putpixel((i, j), (r, g, b))
            j += 1
        i += 1
    
    image.save(file('out.jpg','w'))
    

newImg = Image.new('RGB', (32, 16),(255, 255, 255))
#newImg.save(file('out.jpg','w'))
#byPaste(newImg)
byPixel(newImg)
