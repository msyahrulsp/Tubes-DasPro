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

def main(data):
    consumable, consumable_hist, gadget, gadget_b_hist, gadget_r_hist, inventory, user = data
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

            elif (cmd == "tambahitem"):
                print("tambahitem")

            elif (cmd == "hapusitem"):
                print("hapusitem")

            elif (cmd == "ubahjumlah"):
                print("ubahjumlah")

            elif (cmd == "pinjam"):
                inventory, gadget, gadget_b_hist = borrowGadget(inventory, gadget, gadget_b_hist, id)

            elif (cmd == "kembalikan"):
                inventory, gadget, gadget_r_hist = returnGadget(inventory, gadget_b_hist, id, inventory)

            elif (cmd == "minta"):
                inventory, consumable, consumable_hist = getConsumable(inventory, consumable, consumable_hist, id)

            elif (cmd == "riwayatpinjam"):
                print("riwayatpinjam")

            elif (cmd == "riwayatkembali"):
                print("riwayatkembali")

            elif (cmd == "riwayatambil"):
                print("riwayatambil")

            elif (cmd == "save"):
                data = [consumable, consumable_hist, gadget, gadget_b_hist, gadget_r_hist, inventory, user]
                saveData(data)

            elif (cmd == "help"):
                print("help")

            elif (cmd == "exit"):
                data = [consumable, consumable_hist, gadget, gadget_b_hist, gadget_r_hist, inventory, user]
                keluar(data, "cmd")

        elif validCmd(cmd, role) == 1:
            print("Anda tidak memiliki akses untuk command ini!")
            print("Silahkan gunakan perintah \"help\" untuk mengetahui anda bisa mengakses command apa saja")
        else:
            print("Command tidak ditemukan")
            print("Silahkan gunakan perintah \"help\" untuk mengetahui anda bisa menggunakan command apa saja")

        input("\nTekan ENTER untuk lanjut")
        system("cls")

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
    # For some reason, ini bisa ngambil latest data dari variabel yang ada di main
    # Jadi tolong jangan diapa2in xdd

    # Tapi sabi dicoba coba buat mainin CTRL + C terus save dan liat
    # apa data yang dah dimasukin sebelum CTRL + C ikut ke save
    data = temp
    keluar(data, "key")