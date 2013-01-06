
class CSVFile:
    
    def __init__(self, filePath, utf8BOM = False):
        self.file = file(filePath, "w")
        if utf8BOM:
            #write BOM title, the UTF-8 csv file can be accept by Excel
            self.file.write('\xEF')
            self.file.write('\xBB')
            self.file.write('\xBF')
        
    def writeColumn(self, obj):
        if obj is not None:
            self.file.write(obj)
        self.file.write(",")
    
    def writeLastColumn(self, obj):
        if obj is not None:
            self.file.write(obj)
    
    def newLine(self):
        self.file.write("\n")
        
    def close(self):
        self.file.flush()
        self.file.close()