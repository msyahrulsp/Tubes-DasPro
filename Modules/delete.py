def delItem(data,id):
    for i in range(len(data)):
        if data[i][0] == id:
            opsi = input(f"Apakah anda yakin ingin menghapus {data[i][1]}? Y?N").lower()
            if opsi == 'y':
                data.pop(i)
            print(data)
            input()
            return data
    print(f"Tidak ada item dengan id: {id}")
    return data



