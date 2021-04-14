from os import system
from Modules.loadsave import saveData

def keluar(data):
    system("cls")
    opt = input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    opts = ["Y", "y", "N", "n"]

    while not opt in opts: # Validasi option dari user
        print("\nInput invalid")
        system("cls")
        print(">>> exit")
        opt = input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    if (opt == "Y") or (opt == "y"):
        print()
        saveData(data)
    exit()