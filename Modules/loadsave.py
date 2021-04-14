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
    return temp # Include header

def loadData(folder):
    tempdata = []
    path = ".\Data\%s" % folder
    for (root, dirs, files) in os.walk(path, topdown=True):
        for x in files:
            a = load("./Data/%s/%s" % (folder, x))
            tempdata.append(a)
    return tempdata # Matriks data data yang ada headernya

def saveData(data):
    files = ["consumable", "consumable_history", "gadget", "gadget_borrow_history", "gadget_return_history", "user"]
    # Buat sekarang, folder belum ada validasi buat format tertentu
    folder = input("Masukkan nama folder penyimpanan: ") # Folder apa ada format tertenu??

    if not os.path.exists(".\Data\%s" % folder):
        os.makedirs(".\Data\%s" % folder)

    print("Saving...")

    for i in range(len(files)): # Saving ke respective filenya
        path = ".\Data\%s\%s.csv" % (folder, files[i])
        with open(path, "w") as f:
            for x in data[i]:
                temp = ";".join(map(str, x))
                f.write(temp)
                f.write("\n")

    print("Data telah disimpan pada folder %s!" % folder)