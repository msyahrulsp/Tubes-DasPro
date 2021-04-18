import search

def addGadget(data,id):
    if search.searchByID(data,id):
        print(f"Gagal menambahkan karena {id} sudah ada")
        return data
    nama = input("Masukan Nama                 : ")   
    desc = input("Masukan Deskripsi            : ")
    jlh = input("Masukan Jumlah               : ")
    rare = input("Masukan Rarity               : ")
    year = input("Masukan Tahun Ditemukan      : ")
    print('Item telah berhasil ditambahkan ke database')
    return data.append([id,nama,desc,jlh,rare,year])


def addConsumable(data,id):
    if search.searchByID(data,id):
        print(f"Gagal menambahkan karena {id} sudah ada")
        return data
    nama = input("Masukan Nama                 : ")   
    desc = input("Masukan Deskripsi            : ")
    jlh = input("Masukan Jumlah               : ")
    rare = input("Masukan Rarity               : ")
    print('Item telah berhasil ditambahkan ke database')
    return data.append([id,nama,desc,jlh,rare])

