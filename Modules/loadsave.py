import os
from Util.split import split

def load(filename):
    # { I.S. : Menerima input filename }
    # { F.S. : Data pada filename terload }

    # KAMUS
    # line : array of data
    # temp : array of array of line
    # f : SEQFILE of
    #    (*) temp
    #    (1) mark

    # ALGORITMA
    # Load diganti dari sebelumnya karena banyak "\n" kalau pake readlines
    temp = [] 
    with open(filename, "r") as f:
        for line in f:
            line = line.replace("\n", "")
            line = split(line)
            temp.append(line)
    return temp # Include header

def loadData(folder):
    # { I.S. : Menerima input folder }
    # { F.S. : Data pada folder terload }

    # KAMUS
    # line : array of data
    # tempdata : array of array of line
    # f : SEQFILE of
    #    (*) tempdata
    #    (1) mark
    # files : array of string

    # ALGORITMA
    tempdata = []
    files = ["consumable", "consumable_history", "deleted", "gadget", "gadget_borrow_history", "gadget_return_history", "inventory", "user"]
    for pep in files:
        a = load(f"./Data/{folder}/{pep}.csv")
        tempdata.append(a)
    return tempdata # Matriks data data yang ada headernya

def saveData(data):
    # { I.S. : Menerima input folder }
    # { F.S. : Data pada folder terload }

    # KAMUS
    # files : array of string
    # folder : string

    # ALGORITMA
    files = ["consumable", "consumable_history", "deleted", "gadget", "gadget_borrow_history", "gadget_return_history", "inventory", "user"]
    folder = input("Masukkan nama folder penyimpanan: ")

    if not os.path.exists("./Data/%s" % folder):
        os.makedirs("./Data/%s" % folder)

    print("Saving...")

    for i in range(len(files)): # Saving ke respective filenya
        path = "./Data/%s/%s.csv" % (folder, files[i])
        with open(path, "w") as f:
            for x in data[i]:
                temp = ";".join(map(str, x))
                f.write(temp)
                f.write("\n")

    print("Data telah disimpan pada folder %s!" % folder)