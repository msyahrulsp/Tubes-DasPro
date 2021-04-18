from Util.split import split

def delItem(data,id):
    for i in range(len(data)):
        datasplit=split(data)
        if datasplit[0] == id:
            opsi = input(f"Apakah anda yakin ingin menghapus {datasplit[1]}? Y?N").lower()
            if opsi == 'y':
                data.pop(i)
                return data
            else : return data
    print(f"Tidak ada item dengan id: {id}")
    return data



