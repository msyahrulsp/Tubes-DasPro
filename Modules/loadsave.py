import os
from Util.split import split

def load(filename):
    # Load diganti dari sebelumnya karena banyak "\n" kalau pake readlines
    temp = [] 
    with open(filename, "r") as f:
        for line in f:
            line = line.replace("\n", "")
            line = split(line)
            temp.append(line)
    return temp[1:]

def loadData(folder):
    tempdata = []
    path = ".\Data\%s" % folder
    for (root, dirs, files) in os.walk(path, topdown=True):
        for x in files:
            a = load("./Data/%s/%s" % (folder, x))
            tempdata.append(a)
    return tempdata


def saveData(filename,data):
    f = open(filename, "w")
    f.write(data)
    f.close()