from Modules import search

validRarity = ["C", "B", "A", "S"]

def checkInteger(val):
    try :
        int(val)
        return True
    except ValueError:
        return False


def addGadget(data,id):
    if search.searchByID(data,id):
        print(f"\nGagal menambahkan karena {id} sudah ada")
        input("Tekan Enter untuk melanjutkan")
        return data
    nama = input("Masukan Nama: ")   
    desc = input("Masukan Deskripsi: ")
    jlh = input("Masukan Jumlah: ")
    if checkInteger(jlh) is False or jlh<0:
        print("Jumlah tidak valid")
        input("Tekan Enter untuk melanjutkan")
        return data
    rare = input("Masukan Rarity: ")
    if not (rare in validRarity):
        print("\nInput rarity tidak valid!")
        input("Tekan Enter untuk melanjutkan")
        return data
    year = input("Masukan Tahun Ditemukan: ")
    if checkInteger(jlh) is False or jlh<0:
        print("Tahun tidak valid")
        input("Tekan Enter untuk melanjutkan")
        return data
    print('\nItem telah berhasil ditambahkan ke database')
    return data.append([id,nama,desc,jlh,rare,year])


def addConsumable(data,id):
    if search.searchByID(data,id):
        print(f"\nGagal menambahkan karena {id} sudah ada")
        return data
    nama = input("Masukan Nama: ")   
    desc = input("Masukan Deskripsi: ")
    jlh = input("Masukan Jumlah: ")
    if checkInteger(jlh) is False or jlh<0:
        print("Jumlah tidak valid")
        input("Tekan Enter untuk melanjutkan")
        return data
    rare = input("Masukan Rarity: ")
    if not (rare in validRarity):
        print("\nInput rarity tidak valid!")
        return data
    print('\nItem telah berhasil ditambahkan ke database')
    return data.append([id,nama,desc,jlh,rare])
