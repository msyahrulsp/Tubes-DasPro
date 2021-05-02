from Util.validasi import getId, validDate, validQty

def getConsumable(datacs, datah, invent, userid):
    # { I.S. : Menerima input data consumable, data history minta consumable dan id user}
    # { F.S. : Menghasilkan entry tambahan pada history minta consumable dan mengurangi jumlah item pada consumable yang telah dipilih }

    # KAMUS
    # consuid, date, id : string
    # idx, qty : integer

    # ALGORITMA

    # datacs = list consumable
    # datah = list history minta consumable
    # userid = ngambil dari hasil login
    consuid = input("Masukkan ID item: ")
    idx = getId(datacs, consuid) # Ngambil id consumable sesuai consuid

    if idx == -1:
        print("Consumable dengan ID tersebut tidak ada")
    else:

        qty = input("Jumlah: ")
        if not (validQty(datacs, qty, idx)):
            if(datacs[idx][3] == 0):
                print("%s sedang tidak ada stok" % datacs[idx][1])
            else:
                print("\n%s hanya ada %s" % (datacs[idx][1], datacs[idx][3]))
        elif int(qty) <= 0:
            print("Jumlah yang dimasukkan harus lebih dari 0")
            
        else:
            date = input("Tanggal permintaan (DD/MM/YYYY): ")
            if not (validDate(date)):
                print("Tanggal yang anda masukkan tidak valid")

            else:
                # Auto id buat cons_hist
                if len(datah)-1 == 0:
                    id = "1"
                else:
                    id = str(int(datah[len(datah)-1][0]) + 1)

                print("\nItem %s (x%s) telah berhasil diambil!" % (datacs[idx][1], qty))
                datacs[idx][3] = str(int(datacs[idx][3]) - int(qty)) # Ngurangin jumlah di consumable
                datah.append([id, userid, consuid, date, qty]) # Nambah ke variabel cons history

                # Auto id buat invent
                if len(invent)-1 == 0:
                    id = "1"
                else:
                    id = str(int(invent[len(invent)-1][0]) + 1)
                consuname = datacs[idx][1] # Nama consumable
                rarity = datacs[idx][4] # Rarity
                invent.append([id, consuid, consuname, userid, rarity, qty])

    return datacs, datah, invent