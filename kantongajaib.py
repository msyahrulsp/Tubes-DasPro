import argparse
from Modules.loadsave import loadData
from Modules.login import login
from Util.validasi import validFolder, validCmd

def main():
    parser = argparse.ArgumentParser(usage="python kantongajaib.py <nama_folder>")
    parser.add_argument("folder")
    args = parser.parse_args()

    if not validFolder(args.folder):
        print("Folder yang anda masukkan tidak ada!")
        exit()

    consumable, consumable_hist, gadget, gadget_b_hist, gadget_r_hist, user = loadData(args.folder)
    role = str(login(user))

    while True:
        cmd = input(">>> ").lower().replace(" ", "").replace("_", "")
        if validCmd(cmd, role) == 2: # Masih harus di fix
            if (cmd == "register"):
                print("register")
            elif (cmd == "carirarity"):
                print("carirarity")
            elif (cmd == "caritahun"):
                print("caritahun")
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