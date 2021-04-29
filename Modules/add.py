from Modules import search

#Kamus
# Kelas Kelompok
# Nomor Kelompok
#Nama Anggota           : 1. 16520490 - Farhandika Zahrir Mufti Guenia
#                         2. 16520430 - M. Syahrul Surya Putra
#                         3. 16520120 - Yakobus Iryanto Prasethio
#                         4. 16520370 - Muhammad Rifqi Riansyah M

validRarity = ["C", "B", "A", "S"]

def checkInteger(val):
    try :
        int(val)
        return True
    except ValueError:
        return False

# Prosedur F05 - addGadget dan addConsumable
# Akses : Admin, User
''' Spesifikasi :  Prodesur ini menambahkan data baru ke dalam data consumable atau gadget jika syarat-syaratnya terpenuhi. 
                   Syarat berupa ID yang unique, jumlah dalam bentukan integer dan >= 0, nilai rare yang terdapat di ValidRarirty, dan
                   khusus gadget, tahun wajib dalam integer atau >= 0

'''
# I.S. : data yang menjadi parameter pada fungsi adalah data yang akan ditambahkan dan id yang menjadi parameter pada fungsi akan digunakan
# F.S. : data yang menjadi parameter fungsi ditambahkan dengan data terbaru
# Proses : Mengecek apakah id (parameter Fungsi)is unique, jlh dan year dalam Integer, dan rare terdapat di validRarity, jika semuanya terpenuhi, data yang abru akan di merge ke dalam data yang lama

# Kamus Lokal
''' 
nama : String
desc : String
jlh : integer
rare : char
year : Integer
'''


def addGadget(data,id):
    if search.searchByID(data,id):
        print(f"\nGagal menambahkan karena {id} sudah ada")
        input("Tekan Enter untuk melanjutkan")
        return data
    nama = input("Masukan Nama: ")   
    desc = input("Masukan Deskripsi: ")
    jlh = input("Masukan Jumlah: ")
    if checkInteger(jlh) is False or int(jlh<0):
        print("Jumlah tidak valid")
        input("Tekan Enter untuk melanjutkan")
        return data
    rare = input("Masukan Rarity: ")
    if not (rare in validRarity):
        print("\nInput rarity tidak valid!")
        input("Tekan Enter untuk melanjutkan")
        return data
    year = input("Masukan Tahun Ditemukan: ")
    if checkInteger(year) is False or int(year<0):
        print("Tahun tidak valid")
        input("Tekan Enter untuk melanjutkan")
        return data
    print('\nItem telah berhasil ditambahkan ke database')
    return data.append([id,nama,desc,jlh,rare,year])

# Kamus Lokal
''' 
nama : String
desc : String
jlh : integer
rare : char
'''

def addConsumable(data,id):
    if search.searchByID(data,id):
        print(f"\nGagal menambahkan karena {id} sudah ada")
        return data
    nama = input("Masukan Nama: ")   
    desc = input("Masukan Deskripsi: ")
    jlh = input("Masukan Jumlah: ")
    if checkInteger(jlh) is False or int(jlh<0):
        print("Jumlah tidak valid")
        input("Tekan Enter untuk melanjutkan")
        return data
    rare = input("Masukan Rarity: ")
    if not (rare in validRarity):
        print("\nInput rarity tidak valid!")
        return data
    print('\nItem telah berhasil ditambahkan ke database')
    return data.append([id,nama,desc,jlh,rare])
