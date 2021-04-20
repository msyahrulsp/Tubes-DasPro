from Util.validasi import getId, validDate, validQty

def getConsumable(datacs, datah, userid):
    # datacs = list consumable
    # datah = list history minta consumable
    # userid = ngambil dari hasil login
    consuid = input("Masukkan ID item: ")
    idx = getId(datacs, consuid)

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
                    id = str(int(datah[len(datah)-1][0] + 1))

                print("\nItem %s (x%s) telah berhasil diambil!" % (datacs[idx][1], qty))
                datacs[idx][3] = str(int(datacs[idx][3]) - int(qty)) # Ngurangin jumlah di consumable
                datah.append([id, userid, consuid, date, qty]) # Nambah ke variabel cons history

    return datacs, datah