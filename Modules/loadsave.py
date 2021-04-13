import os

def load(filename):
    data = open(filename, "r")
    lines = data.readlines()
    data.close()
    return lines[1:] # expected output is in array

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
