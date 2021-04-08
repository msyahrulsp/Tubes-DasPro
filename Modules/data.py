import csv
from csv import DictWriter
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

def appendData(filename,field_names,mydict):
    data = open(filename,'a')
    dict = mydict
    dictwriter_object = DictWriter(data, fieldnames=field_names)
    dictwriter_object.writerow(dict)
    data.close()




