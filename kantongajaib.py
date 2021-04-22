import argparse
from os import system
from Modules.loadsave import loadData, saveData
from Modules.keluar import keluar
from Modules.login import login
from Modules.register import register
from Modules.search import searchByRarity, searchByYear
from Modules.gadget import borrowGadget, returnGadget
from Modules.consumable import getConsumable
from Util.validasi import validFolder, validCmd
from Modules.add import addConsumable,addGadget
from Modules.delete import delItem
from Modules.editstock import editStock

def main(data):
    consumable, consumable_hist, deleted, gadget, gadget_b_hist, gadget_r_hist, user = data
    id, role = login(user)

    while (role == "1") or (role == "0"): # Validasi login
        system("cls")
        if (role == "0"): # Username tidak terdaftar
            print("Username tidak terdaftar\n")
        else: # Error = 1, password salah
            print("Password yang anda masukkan salah\n")
        id, role = login(user)

    input("\nTekan ENTER untuk lanjut")
    system("cls")

    while True:
        cmd = input(">>> ").lower().replace(" ", "").replace("_", "")

        if validCmd(cmd, role) == 2: # User punya akses ke cmd

            if (cmd == "register"):
                newUser = register(user)
                if (newUser != ['0']):
                    user.append(newUser)

            elif (cmd == "carirarity"):
                rarity = input("Masukkan rarity: ")
                searchByRarity(gadget, rarity)

            elif (cmd == "caritahun"):
                year = int(input("Masukkan tahun: "))
                cat = input("Masukkan kategori: ")
                searchByYear(gadget, year, cat)

            elif (cmd == "tambahitem"):
                itemid = input('Masukan ID: ')
                if itemid[0] == 'G':
                        gadget = addGadget(gadget,itemid)
                elif itemid[0] == 'C':
                        consumable = addConsumable(consumable,itemid)
                else : print('Gagal menambahkan karena id tidak valid')

            elif (cmd == "hapusitem"):
                itemid = input('Masukan ID Item: ')
                if itemid[0] == 'G':
                        tempdata = [gadget, deleted]
                        gadget, deleted = delItem(tempdata,itemid, "gadget")
                elif itemid[0] == 'C':
                        consumable = delItem(consumable,itemid, "consumable")
                else : print('id tidak valid')
            
            elif (cmd == "ubahjumlah"):
                itemid = input("Masukkan ID: ")
                if iditem[0] =="G":
                    gadget = editStock(gadget,itemid)
                elif iditem[0] == "C":
                    consumable = editStock(consumable,itemid)
                else:
                    print("Tidak ada item dengan ID tersebut!")

            elif (cmd == "pinjam"):
                gadget, gadget_b_hist = borrowGadget(gadget, gadget_b_hist, id)

            elif (cmd == "kembalikan"):
                gadget, gadget_b_hist, gadget_r_hist, deleted = returnGadget(gadget, gadget_b_hist, gadget_r_hist, deleted, id)

            elif (cmd == "minta"):
                consumable, consumable_hist = getConsumable(consumable, consumable_hist, id)

            elif (cmd == "riwayatpinjam"):
                print("riwayatpinjam")

            elif (cmd == "riwayatkembali"):
                print("riwayatkembali")

            elif (cmd == "riwayatambil"):
                print("riwayatambil")

            elif (cmd == "save"):
                data = [consumable, consumable_hist, deleted, gadget, gadget_b_hist, gadget_r_hist, user]
                saveData(data)

            elif (cmd == "help"):
                print("help")

            elif (cmd == "exit"):
                data = [consumable, consumable_hist, deleted, gadget, gadget_b_hist, gadget_r_hist, user]
                keluar(data, "cmd")

        elif validCmd(cmd, role) == 1: # User gk ada akses
            print("\nAnda tidak memiliki akses untuk command ini!")
            print("Silahkan gunakan perintah \"help\" untuk mengetahui anda bisa mengakses command apa saja")

        else: # Command gk ada di list
            print("\nCommand tidak ditemukan")
            print("Silahkan gunakan perintah \"help\" untuk mengetahui anda bisa menggunakan command apa saja")

        input("\nTekan ENTER untuk lanjut")
        system("cls")

try:
    system("cls")
    parser = argparse.ArgumentParser(usage="python kantongajaib.py <nama_folder>") # Error messagenya masih belum custom
    parser.add_argument("folder")
    args = parser.parse_args()

    if not validFolder(args.folder): # Folder harus ada di path Data/
        print("Folder yang anda masukkan tidak ada!")
        exit()

    temp = loadData(args.folder) # Ngeload file dari folder yang dah dimasukin pas ngejalanin
    # Catetan : ini nge load pake header, jadi kalau mau make, di slice dlu index 0nya

    main(temp)
except KeyboardInterrupt: # Bakal aktif kalau pake CTRL + C
    # For some reason, ini bisa ngambil latest data dari variabel yang ada di main
    # Jadi tolong jangan diapa2in xdd

    # Tapi sabi dicoba coba buat mainin CTRL + C terus save dan liat
    # apa data yang dah dimasukin sebelum CTRL + C ikut ke save
    data = temp
    keluar(data, "key")
