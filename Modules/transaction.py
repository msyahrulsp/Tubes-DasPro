from Util.validasi import validId, validDate, validQty

def borrowGadget(datagd, datah, userid):
    # datagd = list gadget
    # datah = list history borrow gadget
    # userid = ngambil dari hasil login
    gadgetid = input("Masukkan ID item: ")
    idx = validId(datagd, gadgetid)

    if idx == -1:
        print("Gadget dengan ID tersebut tidak ada")
        return datagd, datah
    else:
        date = input("Tanggal peminjaman (DD/MM/YYYY): ")
        if not (validDate(date)):
            print("Tanggal yang anda masukkan tidak valid")
            return datagd, datah
        else:
            qty = input("Jumlah peminjaman: ")
            if not (validQty(datagd, qty, idx)):
                print("Jumlah yang anda pinjam melebihi stok yang kami punya")
                return datagd, datah
            elif (int(qty) <= 0):
                print("Jumlah yang dimasukkan harus lebih dari 0")
                return datagd, datah
            else:
                if len(datah)-1 == 0:
                    id = "1"
                else:
                    id = str(int(datah[len(datah)-1][0]) + 1)

                print("\nItem %s (x%s) berhasil dipinjam!" % (datagd[idx][1], qty))
                datagd[idx][3] = str(int(datagd[idx][3]) - int(qty)) # Ngurangin jumlah di consumable
                datah.append([id, userid, gadgetid, date, qty]) # Nambah value ke gadget borrow history
                return datagd, datah

def returnGadget(data, userid): # In Progress
    temp = []
    i = 1
    for x in data:
        if x[1] == userid:
            temp.append(x)
            print("%d. %s" % (i, x))

def getConsumable(datacs, datah, userid):
    # datacs = list consumable
    # datah = list history minta consumable
    # userid = ngambil dari hasil login
    consuid = input("Masukkan ID item: ")
    idx = validId(datacs, consuid)

    if idx == -1:
        print("Consumable dengan ID tersebut tidak ada")
        return datacs, datah
    else:
        qty = input("Jumlah peminjaman: ")
        if not (validQty(datacs, qty, idx)):
            print("Jumlah yang anda minta melebihi stok yang kami punya")
            return datacs, datah
        elif int(qty) <= 0:
            print("Jumlah yang dimasukkan harus lebih dari 0")
            return datacs, datah
        else:
            date = input("Tanggal peminjaman (DD/MM/YYYY): ")
            if not (validDate(date)):
                print("Tanggal yang anda masukkan tidak valid")
                return datacs, datah
            else:
                if len(datah)-1 == 0:
                    id = "1"
                else:
                    id = str(int(datah[len(datah)-1][0] + 1))

                print("\nItem %s (x%s) telah berhasil diambil!" % (datacs[idx][1], qty))
                datacs[idx][3] = str(int(datacs[idx][3]) - int(qty)) # Ngurangin jumlah di consumable
                datah.append([id, userid, consuid, date]) # Nambah ke variabel cons history
                return datacs, datah