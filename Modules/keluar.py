from os import system
from Modules.loadsave import saveData

def keluar(data, type, role):
    # { I.S. : Menerima input berupa semua data, tipe exit, dan role user}
    # { F.S. : Keluar program sesuai dengan tipe dan jika role tidak admin/user, tidak bisa menjalankan prosedur save}

    # KAMUS
    # opt : string

    # ALGORITMA
    system("cls")

    if type == "cmd": # in case pake cmd >>> exit, ditambah print >>> exit
        print(">>> exit")
        
    opt = input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ").lower()
    if (opt != "y") and (opt != "n"):
        input("\nInput invalid")
        return keluar(data, type, role)
    
    if opt == 'y':
        if role == "nouser":
            print("\nAnda tidak memiliki akses untuk save")
        else:
            print()
            saveData(data)
    exit()