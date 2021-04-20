import argparse
from os import system
from Modules.loadsave import loadData, saveData
from Modules.keluar import keluar
from Modules.login import login
from Modules.register import register
from Modules.search import searchByRarity, searchByYear
from Modules.transaction import borrowGadget, returnGadget, getConsumable
from Util.validasi import validFolder, validCmd
from Modules.add import addConsumable,addGadget
from Modules.delete import delItem

def main(data):
    consumable, consumable_hist, gadget, gadget_b_hist, gadget_r_hist, user = data
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

        if validCmd(cmd, role) == 2:

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

            elif (cmd == "tambahitem"): #masih dalam perbaikan, kudu di cek duls gan
                itemid = input('Masukan Index       : ')
                if itemid[0] == 'G':
                        gadget = addGadget(gadget,itemid)
                elif itemid[0] == 'C':
                        consumable = addConsumable(consumable,itemid)
                else : print('Gagal menambahkan karena id tidak valid')

            elif (cmd == "hapusitem"):
                itemid = input('Masukan Index       : ')
                if itemid[0] == 'G':
                        tempdata = [gadget, deleted]
                        gadget, deleted = delItem(tempdata,itemid, "gadget")
                elif itemid[0] == 'C':
                        consumable = delItem(consumable,itemid, "consumable")
                else : print('id tidak valid')
            
            elif (cmd == "ubahjumlah"):
                print("ubahjumlah")

            elif (cmd == "pinjam"):
                gadget, gadget_b_hist = borrowGadget(gadget, gadget_b_hist, id)

            elif (cmd == "kembalikan"):
                # returnGadget(gadget_b_hist, id)
                print("Panggil returnGadget")

            elif (cmd == "minta"):
                consumable, consumable_hist = getConsumable(consumable, consumable_hist, id)

            elif (cmd == "riwayatpinjam"):
                print("riwayatpinjam")

            elif (cmd == "riwayatkembali"):
                print("riwayatkembali")

            elif (cmd == "riwayatambil"):
                print("riwayatambil")

            elif (cmd == "save"):
                data = [consumable, consumable_hist, gadget, gadget_b_hist, gadget_r_hist, user]
                saveData(data)

            elif (cmd == "help"):
                print("help")

            elif (cmd == "exit"):
                data = [consumable, consumable_hist, gadget, gadget_b_hist, gadget_r_hist, user]
                keluar(data)

            input("\nTekan ENTER untuk lanjut")
            system("cls")

        elif validCmd(cmd, role) == 1:
            print("Anda tidak memiliki akses untuk command ini!")
        else:
            print("Command tidak ditemukan")

try:
    system("cls")
    parser = argparse.ArgumentParser(usage="python kantongajaib.py <nama_folder>") # Error messagenya masih belum custom
    parser.add_argument("folder")
    args = parser.parse_args()

    if not validFolder(args.folder):
        print("Folder yang anda masukkan tidak ada!")
        exit()

    temp = loadData(args.folder) # Ngeload file dari folder yang dah dimasukin pas ngejalanin
    # Catetan : ini nge load pake header, jadi kalau mau make, di slice dlu index 0nya

    main(temp)
except KeyboardInterrupt: # Bakal aktif kalau pake CTRL + C
    data = temp
    keluar(data)