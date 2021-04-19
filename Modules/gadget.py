from Util.validasi import getId, validDate, validQty
from Util.gadget import checkGadget, userGadget

def borrowGadget(invent, datagd, datah, userid):
    # datagd = list gadget
    # datah = list history borrow gadget
    # userid = ngambil dari hasil login
    gadgetid = input("Masukkan ID item: ") # Gk bisa minjem gadget yang sama

    if not checkGadget(invent, gadgetid, userid):
        print("Anda sedang meminjam gadget tersebut")
        return invent, datagd, datah
    
    idx = getId(datagd, gadgetid)

    if idx == -1:
        print("Gadget dengan ID tersebut tidak ada")
    else:
        date = input("Tanggal peminjaman (DD/MM/YYYY): ")
        if not (validDate(date)):
            print("Tanggal yang anda masukkan tidak valid")
        else:
            qty = input("Jumlah peminjaman: ")
            if not (validQty(datagd, qty, idx)):
                print("Jumlah yang anda pinjam melebihi stok yang kami punya")
            elif (int(qty) <= 0):
                print("Jumlah yang dimasukkan harus lebih dari 0")
            else:
                if len(datah)-1 == 0:
                    id = "1"
                else:
                    id = str(int(datah[len(datah)-1][0]) + 1)

                print("\nItem %s (x%s) berhasil dipinjam!" % (datagd[idx][1], qty))
                datagd[idx][3] = str(int(datagd[idx][3]) - int(qty)) # Ngurangin jumlah di consumable
                datah.append([id, userid, gadgetid, date, qty]) # Nambah value ke gadget borrow history
        
    return invent, datagd, datah

def returnGadget(invent, datag, datah, userid): # In Progress
    # gadget.csv, gadget_return.csv, inventory, 
    tempinvent = userGadget(userid, invent) # Ngeload inventory user spesifik dari inventory.csv
    
    print()
    for i in range(len(tempinvent)):
        print("%d. %s" % (i+1, tempinvent[i][3]))
        
    if (len(tempinvent) == 0):
        print("Kamu belum meminjam gadget apapun")
    else:
        opt = int(input("\nMasukkan nomor peminjaman: "))
        if (opt <= 0) and (opt > len(tempinvent)):
            print("Pilihan yang anda masukkan tidak valid")
        else:
            # ambil index si gadget di gadget_csv
            date = input("Tanggal pengembalian (DD/MM/YYYY): ")
            if not (validDate(date)):
                print("Tanggal yang anda masukkan tidak valid")
            else:
                qty = input("Banyak item yang mau dikembalikan: ")
                if not (validQty):
                    print("Jumlah yang anda masukkan tidak valid")
                elif (int(qty) <= 0):
                    print("Jumlah yang dimasukkan harus lebih dari 0")
                else:
                    if len(datah)-1 == 0:
                        id = "1"
                    else:
                        id = str(int(datah[len(datah)-1][0]) + 1)

                    print("\nItem %s (x%s) berhasil dikembalikan" % (invent[i][4], qty))
                    datah.append([id, idpeminjaman, date, isreturned])
                    # Kalau habis, delete sama ganti isreturned

    return invent, datag, datah