class FileLoader:
    def __init__(self, filename):
        self.filename = filename

    def readFile(self):
        r = open(self.filename, 'rb')
        data = r.read()
        r.close()
        return data
    
    def writeFile(self, data):
        r = open(self.filename, 'wb')
        r.write(data)
        r.close()
    