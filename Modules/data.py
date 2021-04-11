

#import split

def loadData(filename):
    data = open(filename, "r")
    lines = data.readlines()
    data.close()
    return lines

def saveData(filename,data):
    f = open(filename, "w")
    f.write(data)
    f.close()






