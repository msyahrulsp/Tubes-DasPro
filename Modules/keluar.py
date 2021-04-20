from os import system
from Modules.loadsave import saveData

def keluar(data, type):
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
        print()
        saveData(data)
    exit()