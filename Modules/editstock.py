#Module
from Util.validasi import getId

def editStock(data,id):
    idx = getId(data, id)
    if idx == -1:
        print("Tidak ada item dengan ID tersebut!")
        return data
    else:
        jmlh = int(input("Masukkan Jumlah: "))
        if (jmlh<0) and (data[idx][3]<abs(jmlh)):
            print(f"{jmlh} {data[idx][1]} gagal dibuang karena stok kurang. Stok sekarang: {data[idx][3]} (< {jmlh})")
            return data
        elif jmlh>=0:
            print(f"{jmlh} {data[idx][1]} berhasil ditambahkan. Stok sekarang: {data[idx][3]+jmlh}")
            data[idx][3] = str(int(data[idx][3] + jmlh))
        elif jmlh <0:
            print(f"{jmlh} {data[idx][1]} berhasil dibuang. Stok sekarang: {data[idx][3] + jmlh}")
            data[idx][3] = str(int(data[idx][3] + jmlh))
    return data




