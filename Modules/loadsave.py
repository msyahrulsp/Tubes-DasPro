import os
from Util.split import split

types = ["consumable", "consumable_history", "deleted", "gadget", "gadget_borrow_history", "gadget_return_history", "inventory", "user"]

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
    for pep in types:
        a = load(f"./Data/{folder}/{pep}.csv")
        tempdata.append(a)
    return tempdata # Matriks data data yang ada headernya

def saveIt(datas,path):
    with open(path,'w') as f:
        [f.write(';'.join(map(str,data)) + '\n') for data in datas]
    f.close()

def saveData(data):
    # { I.S. : Menerima input folder }
    # { F.S. : Data pada folder terload }

    # KAMUS
    # files : array of string
    # folder : string

    # ALGORITMA
    folder = input("Masukkan nama folder penyimpanan: ")

    if not os.path.exists("./Data/%s" % folder):
        os.makedirs("./Data/%s" % folder)


    for i in range(len(types)): # Saving ke respective filenya
        print(f"Saving {types[i]}")
        saveIt(data[i],"./Data/%s/%s.csv" % (folder, types[i]))

    print("Data telah disimpan pada folder %s!" % folder)

