from Modules import search

validRarity = ["C", "B", "A", "S"]

def addGadget(data,id):
    if search.searchByID(data,id):
        print(f"\nGagal menambahkan karena {id} sudah ada")
        return data
    nama = input("Masukan Nama                 : ")   
    desc = input("Masukan Deskripsi            : ")
    jlh = input("Masukan Jumlah               : ")
    rare = input("Masukan Rarity               : ")
    if not (rare in validRarity):
        print("\nInput rarity tidak valid!")
        return addGadget(data,id)
    year = input("Masukan Tahun Ditemukan      : ")
    print('Item telah berhasil ditambahkan ke database')
    return data+[[id,nama,desc,jlh,rare,year]]


def addConsumable(data,id):
    if search.searchByID(data,id):
        print(f"\nGagal menambahkan karena {id} sudah ada")
        return data
    nama = input("Masukan Nama                 : ")   
    desc = input("Masukan Deskripsi            : ")
    jlh = input("Masukan Jumlah               : ")
    rare = input("Masukan Rarity               : ")
    if not (rare in validRarity):
        print("\nInput rarity tidak valid!")
        return addConsumable(data,id)
    print('Item telah berhasil ditambahkan ke database')
    return data+[[id,nama,desc,jlh,rare]]

