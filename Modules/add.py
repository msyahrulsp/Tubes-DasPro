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
    year = input("Masukan Tahun Ditemukan      : ")
<<<<<<< HEAD
    print('Item telah berhasil ditambahkan ke database')
    return data+[[id,nama,desc,jlh,rare,year]]
=======
    print('\nItem telah berhasil ditambahkan ke database')
    return data.append([id,nama,desc,jlh,rare,year])
>>>>>>> 077d323ececff01d4693b388b05e0830cb0f15f7


def addConsumable(data,id):
    if search.searchByID(data,id):
        print(f"\nGagal menambahkan karena {id} sudah ada")
        return data
    nama = input("Masukan Nama                 : ")   
    desc = input("Masukan Deskripsi            : ")
    jlh = input("Masukan Jumlah               : ")
    rare = input("Masukan Rarity               : ")
<<<<<<< HEAD
    print('Item telah berhasil ditambahkan ke database')
    return data+[[id,nama,desc,jlh,rare]]
=======
    if not (rare in validRarity):
        print("\nInput rarity tidak valid!")
    print('\nItem telah berhasil ditambahkan ke database')
    return data.append([id,nama,desc,jlh,rare])
>>>>>>> 077d323ececff01d4693b388b05e0830cb0f15f7

