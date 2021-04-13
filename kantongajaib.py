import argparse
from Modules.loadsave import loadData
from Modules.login import login
from Modules.register import register
from Modules.search import searchByRarity, searchByYear
from Util.validasi import validFolder, validCmd

def main():
    parser = argparse.ArgumentParser(usage="python kantongajaib.py <nama_folder>")
    parser.add_argument("folder")
    args = parser.parse_args()

    if not validFolder(args.folder):
        print("Folder yang anda masukkan tidak ada!")
        exit()

    consumable, consumable_hist, gadget, gadget_b_hist, gadget_r_hist, user = loadData(args.folder)
    id, role = login(user)

    while True:
        cmd = input(">>> ").lower().replace(" ", "").replace("_", "")
        if validCmd(cmd, role) == 2:
            if (cmd == "register"):
                newUser = register(user)
                if (newUser != ['0']):
                    user.append(newUser)
                print(user)
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
                print("pinjam")
            elif (cmd == "kembalikan"):
                print("kembalikan")
            elif (cmd == "minta"):
                print("minta")
            elif (cmd == "riwayatpinjam"):
                print("riwayatpinjam")
            elif (cmd == "riwayatkembali"):
                print("riwayatkembali")
            elif (cmd == "riwayatambil"):
                print("riwayatambil")
            elif (cmd == "save"):
                print("save")
            elif (cmd == "help"):
                print("help")
            elif (cmd == "exit"):
                print("exit")
        elif validCmd(cmd, role) == 1:
            print("Anda tidak memiliki akses untuk command ini!")
        else:
            print("Command tidak ditemukan")

try:
    main()
except KeyboardInterrupt:
    print("Panggil function exit")