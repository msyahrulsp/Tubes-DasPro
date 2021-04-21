import os
from datetime import datetime

def validFolder(folder):
    for (root, dirs, files) in os.walk('./Data', topdown=True):
        if folder in dirs:
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

def getId(data, id): # Cek validasi sekalian return idx kalau true
    for i in range(1, len(data)):
        if data[i][0] == id : return i
    return -1 

def validDate(date): # Cek validasi tanggal (DD/MM/YYYY)
    try:
        date = datetime.strptime(date, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def validQty(data, qty, idx): # Ngebandingin inputan qty user sama qty yang ada di inventory
    qty = int(qty)
    if int(data[idx][3]) < qty:
        return False
    return True