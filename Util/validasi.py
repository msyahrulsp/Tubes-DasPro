import os

def validFolder(folder):
    for (root, dirs, files) in os.walk('.\Data', topdown=True):
        if [folder] == dirs:
            return True
        return False

def validCmd(cmd, role):
    # 0 = Not Found
    # 1 = No Access
    # 2 = True
    adminCmd = ["register", "tambahitem", "hapusitem", "ubahjumlah", "riwayatpinjam", "riwayatkembali", "riwayatambil"]
    bothCmd = ["carirarity", "caritahun", "save", "help", "exit"]
    userCmd = ["pinjam", "kembalikan", "minta"]

    if (role == "admin"):
        if (cmd in adminCmd) or (cmd in bothCmd):
            return 2

    if (role == "user"):
        if (cmd in userCmd) or (cmd in bothCmd):
            return 2

    if (cmd in adminCmd) or (cmd in bothCmd) or (cmd in userCmd):
        return 1
    return 0