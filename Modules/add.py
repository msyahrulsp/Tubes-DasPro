from Modules import search

validRarity = ["C", "B", "A", "S"]

def addGadget(data,id):
    if search.searchByID(data,id):
        print(f"\nGagal menambahkan karena {id} sudah ada")
        return data
    nama = input("Masukan Nama: ")   
    desc = input("Masukan Deskripsi: ")
    jlh = input("Masukan Jumlah: ")
    rare = input("Masukan Rarity: ")
    if not (rare in validRarity):
        print("\nInput rarity tidak valid!")
    year = input("Masukan Tahun Ditemukan: ")
    print('\nItem telah berhasil ditambahkan ke database')
    return data.append([id,nama,desc,jlh,rare,year])


def addConsumable(data,id):
    if search.searchByID(data,id):
        print(f"\nGagal menambahkan karena {id} sudah ada")
        return data
    nama = input("Masukan Nama: ")   
    desc = input("Masukan Deskripsi: ")
    jlh = input("Masukan Jumlah: ")
    rare = input("Masukan Rarity: ")
    if not (rare in validRarity):
        print("\nInput rarity tidak valid!")
    print('\nItem telah berhasil ditambahkan ke database')
    return data.append([id,nama,desc,jlh,rare])

