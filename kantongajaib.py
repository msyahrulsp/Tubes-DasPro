import argparse
from os import system
from Modules.loadsave import loadData, saveData
from Modules.keluar import keluar
from Modules.login import login
from Modules.register import register
from Modules.search import searchByRarity, searchByYear 
from Modules.gadget_borrow_history import gadget_bor_hist
from Modules.gadget_return_history import gadget_ret_hist
from Modules.consumable_history import consum_hist
from Modules.gadget import borrowGadget, returnGadget
from Modules.consumable import getConsumable
from Util.validasi import validFolder, validCmd
from Modules.add import addConsumable,addGadget
from Modules.delete import delItem
from Modules.editstock import editStock
from Modules.help import openHelp
from Modules.gacha import gacha

def main(data):
    consumable, consumable_hist, deleted, gadget, gadget_b_hist, gadget_r_hist, inventory, user = data
    id = -1
    role = "nouser"

    while True:
        if role == "nouser":
            print("Selamat datang di program kami, silakan ketik 'help' atau 'login'")

        cmd = input(">>> ").lower().replace(" ", "").replace("_", "")

        if validCmd(cmd, role) == 2: # User punya akses ke cmd

            if (cmd == "login"):
                system("cls")
                id, role = login(user)
                while (role == "1") or (role == "0"): # Validasi login
                    system("cls")
                    if (role == "0"): # Username tidak terdaftar
                        print("Username tidak terdaftar\n")
                    else: # Error = 1, password salah
                        print("Password yang anda masukkan salah\n")
                    id, role = login(user)

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
                if itemid[0] =="G":
                    gadget = editStock(gadget,itemid)
                elif itemid[0] == "C":
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
                gadget_bor_hist(gadget_b_hist)

            elif (cmd == "riwayatkembali"):
                gadget_ret_hist(gadget_r_hist)

            elif (cmd == "riwayatambil"):
                consum_hist(consumable_hist)

            elif (cmd == "save"):
                data = [consumable, consumable_hist, deleted, gadget, gadget_b_hist, gadget_r_hist, inventory, user]
                saveData(data)

            elif (cmd == "help"):
                openHelp(role) #menggunakan help berdasarkan role pengguna saat ini

            elif (cmd == "exit"):
                data = [consumable, consumable_hist, deleted, gadget, gadget_b_hist, gadget_r_hist, inventory, user]
                keluar(data, "cmd", role)

            elif (cmd == "gacha"):
                inventory, consumable, consumable_hist = gacha(inventory, consumable, consumable_hist, id)

        elif validCmd(cmd, role) == 1: # User gk ada akses
            print("\nAnda tidak memiliki akses untuk command ini!")
            print("Silahkan gunakan perintah \"help\" untuk mengetahui anda bisa mengakses command apa saja")

        else: # Command gk ada di list
            print("\nCommand tidak ditemukan")
            print("Silahkan gunakan perintah \"help\" untuk mengetahui anda bisa menggunakan command apa saja")

        input("\nTekan ENTER untuk lanjut")
        system("cls")

system("cls")
parser = argparse.ArgumentParser(usage="python kantongajaib.py <nama_folder>")
parser.add_argument("folder")
args = parser.parse_args()

if not validFolder(args.folder): # Folder harus ada di path Data/
    print("Folder yang anda masukkan tidak ada!")
    exit()

temp = loadData(args.folder) # Ngeload file dari folder yang dah dimasukin pas ngejalaninh
# Catetan : ini nge load pake header, jadi kalau mau make, di slice dlu index 0nya

main(temp)