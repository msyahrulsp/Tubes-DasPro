from Util.validasi import getId, validDate, validQty
from Util.gadget import checkGadget, userGadget

def borrowGadget(datagd, datah, userid):
    # { I.S. : Menerima input data gadget, data history pinjam gadget dan id user}
    # { F.S. : Menghasilkan entry tambahan pada history pinjam gadget dan mengurangi jumlah item pada gadget yang telah dipilih }

    # KAMUS
    # gadgetid, date, id : string
    # idx, qty : integer

    # ALGORITMA

    # datagd = list gadget
    # datah = list history borrow gadget
    # userid = ngambil dari hasil login

    gadgetid = input("Masukkan ID item: ")

    # Validasi buat gk bisa minjem item yang lagi dipinjem (masih belum di return full)
    if not checkGadget(datah, gadgetid, userid):
        print("Anda sedang meminjam gadget tersebut")
        return datagd, datah
    
    idx = getId(datagd, gadgetid) # Ngambil index dari gadget yang sesuai sama id gadget

    if idx == -1:
        print("Gadget dengan ID tersebut tidak ada")

    else:

        date = input("Tanggal peminjaman (DD/MM/YYYY): ")
        if not (validDate(date)):
            print("Tanggal yang anda masukkan tidak valid")
        else:

            qty = input("Jumlah peminjaman: ")
            if not (validQty(datagd, qty, idx)):
                if (datagd[idx][3] == 0):
                    print("\n%s sedang tidak ada stok" % datagd[idx][1])
                else:
                    print("\nUntuk sekarang %s hanya ada %s" % (datagd[idx][1], datagd[idx][3]))

            elif (int(qty) <= 0):
                print("Jumlah yang dimasukkan harus lebih dari 0")

            else:
                # Auto id buat borrow_hist
                if len(datah)-1 == 0:
                    id = "1"
                else:
                    id = str(int(datah[len(datah)-1][0]) + 1)

                print("\nItem %s (x%s) berhasil dipinjam!" % (datagd[idx][1], qty))
                datagd[idx][3] = str(int(datagd[idx][3]) - int(qty)) # Ngurangin jumlah di consumable
                datah.append([id, userid, gadgetid, date, qty, "0"]) # Nambah value ke gadget borrow history
        
    return datagd, datah

def returnGadget(datag, datahb, datahr, deleted, userid):
    # { I.S. : Menerima input data gadget, data history pinjam gadget, data reurn history gadget, deleted item, dan user id}
    # { F.S. : Menghasilkan entry baru pada gadget (jika item yang dikembalikan telah didelete) atau menambahkan item ke gadget. Dan menambahkan entry
    # pada return history dan mengubah is_returned pada borrow history }

    # KAMUS
    # listtempid : array of integer
    # name, date, id, id_peminjaman, idx_borrow : string
    # tempid, opt, idx, qty, n : integer

    # ALGORITMA
    # datag = list gadget
    # datahb = list gadget borrow history
    # datahr = list gadget return history
    # deleted = list deleted item
    # userid = id dari user 

    pinjamList = userGadget(datahb, userid) # Ngeload gadget yang belum di return dari borrow_history
    listtempid = []

    print()
        
    if (len(pinjamList) == 0):
        print("Anda belum meminjam gadget apapun")
    else:

        # Ngeloop list yang diambil dari borrow_hist dan yang emg blm di return full
        for i in range(len(pinjamList)):
            tempid = getId(datag, pinjamList[i][2]) # gadget, idgadget(dari borrow_hist)
            name = datag[tempid][1] # Nama gadget dari gadget
            if tempid == -1:
                tempid2 = getId(deleted, pinjamList[i][2]) # deleted, idgadget(dari borrow_hist)
                name = deleted[tempid2][1]
            listtempid.append(tempid)
            print("%d. %s" % (i+1, name))

        opt = int(input("\nMasukkan nomor peminjaman: "))
        if (opt <= 0) or (opt > len(pinjamList)):
            print("\nPilihan yang anda masukkan tidak valid")

        else:
            opt -= 1
            idx = listtempid[opt] # Index gadget di gadget.csv)

            # Buat case item yang udah kena delete sebelum di return
            if (idx == -1):
                idx = getId(deleted, pinjamList[opt][2])
                datag.append(deleted[idx]) # Nambahin deleted item ke gadget (karena di return)
                deleted.pop(idx) # Delete deleted item, karena dah di return

                # Auto id baru buat deleted gadget yang bakal di return
                if len(datag)-1 == 1:
                    datag[1][0] = "G1"
                else:
                    datag[len(datag)-1][0] = "G" + str(int(datag[len(datag)-2][0][1]) + 1)
                idx = len(datag)-1 # idx ke last elemen gadget

            date = input("Tanggal pengembalian (DD/MM/YYYY): ")
            if not (validDate(date)):
                print("Tanggal yang anda masukkan tidak valid")

            else:
                qty = input("Banyak item yang mau dikembalikan: ")
                n = int(pinjamList[opt][4]) - int(pinjamList[opt][5]) # Jumlah pinjam - is_returned
                if int(qty) > n:
                    print("\nAnda hanya belum mengembalikan %d %s" % (n, datag[idx][1]))
                elif (int(qty) <= 0):
                    print("Jumlah yang dimasukkan harus lebih dari 0")

                else:
                    # Auto id buat return_hist
                    if len(datahr)-1 == 0:
                        id = "1"
                    else:
                        id = str(int(datahr[len(datahr)-1][0]) + 1)

                    id_peminjaman = pinjamList[opt][0] # Ngambil id_peminjaman
                    print("\nItem %s (x%s) berhasil dikembalikan" % (datag[idx][1], qty))
                    datahr.append([id, id_peminjaman, date, qty]) # Nambah data ke return_history

                    idx_borrow = getId(datahb, id_peminjaman) # Ngambil index dari id_peminjaman yang sesuai
                    datahb[idx_borrow][5] = str(int(datahb[idx_borrow][5]) + int(qty)) # Nambah jumlah is_returned sesuai jumlah return
                    datahb[idx_borrow][2] = datag[idx][0] # Ngubah id deleted gadget di borrow history supaya ngematch id gadget baru
                    datag[idx][3] = str(int(datag[idx][3]) + int(qty)) # Nambah item di gadget sesuai jumlah return

    return datag, datahb, datahr, deleted