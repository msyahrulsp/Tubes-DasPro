from os import system
from Modules.loadsave import saveData

def keluar(data, type, role="nouser"):
    system("cls")

    if type == "cmd": # in case pake cmd >>> exit, ditambah print >>> exit
        print(">>> exit")
        
    opt = input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    opts = ["Y", "y", "N", "n"]

    while not opt in opts: # Validasi option dari user
        input("\nInput invalid")
        system("cls")
        if type == "cmd":
            print(">>> exit")
        opt = input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    if (opt == "Y") or (opt == "y"):
        if role == "nouser":
            print("\nAnda tidak memiliki akses untuk save")
        else:
            print()
            saveData(data)
    exit()