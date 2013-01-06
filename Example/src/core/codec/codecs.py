import codecs

def writeUnicodeToFile():
    s = u'\u7894';
    stream = codecs.open("filename", "w", "utf-8")
    stream.write(s)