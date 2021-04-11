

#import split

#filename = si filenamenya , misal Data/user.csv
# data = si datanya, abis di load, kan jadi array, ntar abis ditambahin, baru deh jadiin string lagi

def loadData(filename):
    data = open(filename, "r")
    lines = data.readlines()
    data.close()
    return lines # expected output is in array

def saveData(filename,data):
    f = open(filename, "w")
    f.write(data)
    f.close()






