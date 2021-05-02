from Util.split import split

#Kamus
# Kelas Kelompok
# Nomor Kelompok
#Nama Anggota           : 1. 16520490 - Farhandika Zahrir Mufti Guenia
#                         2. 16520430 - M. Syahrul Surya Putra
#                         3. 16520120 - Yakobus Iryanto Prasethio
#                         4. 16520370 - Muhammad Rifqi Riansyah M



# Prosedur F06 - Menghapus Consumable atau Gadget / delItem
# Akses : Admin, User
''' Spesifikasi :  Prosedur ini men deteksi apa yang mau di delete (Gadget atau COnsumable), lalu mendeletenya berdasarkan id yang dimasukan oleh user

'''
# I.S. : parameter fungsii pada fungsi ini adalah data, id sebagai alat pencari mana yang mau di delete, dan type sebagai penentu tipe apa yang mau di delete
# F.S. : jika id ada terdapat dalam data, makan akan di delete itemnya berdasarkan id yang dimasukan user
# Proses : 
'''
  akan di loop sebanyak data yang ada, jika matching idnya dengan id inputan user, makan akan diminta apakah user yakin jika ingin di delete, jika iya maka item akan di delete
  dan jika tidak ada yang matching, program akan memeberikan sebuah printout bahwa id tidak ditemukan di dalam sistem          
'''


# Kamus Lokal
''' 
item : Array of Something (bisa int,string,atau char)
deleted : Array of Something
opsi : Char
'''

def delItem(data, id, type):
    if type == "gadget":
        item = data[0] # Gadget
        deleted = data[1] # Deleted
    else:
        item = data # Consumables

    for i in range(len(item)):
        datasplit=item[i]
        if datasplit[0] == id:
            opsi = input(f"Apakah anda yakin ingin menghapus {datasplit[1]} (Y/N)? ").lower()
            if opsi == 'y':
                print("\nItem telah berhasil dihapus dari database")
                if type == "gadget":
                    item[i][3] = "0" # Deleled item langsung punya 0 item
                    deleted.append(item[i])
                    item.pop(i)
                    return item, deleted
                item.pop(i)
                return item
            elif opsi != "n":
                print("\nInput invalid")
             
            if type == "gadget":
                return item, deleted
            return item

    print(f"\nTidak ada item dengan id: {id}")
    
    if type == "gadget":
        return item, deleted
    return item