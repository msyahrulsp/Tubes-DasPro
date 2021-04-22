import datetime

def gadget_bor_hist (data):
    data_length = getDataLen(data)
    current_idx = findLowest(data, data_length)

    for i in range (5):
        idx = getID(data,current_idx[i])
        print("ID Peminjaman: ", idx)

        id_peminjam = getPeminjam(data,current_idx[i])
        print("Nama Pengambil: ", id_peminjam)

        id_gadget = getGadget(data,current_idx[i])
        print("Nama Gadget: ", id_gadget)

        tanggal_pinjam = getDate(data,current_idx[i])
        print("Tanggal Peminjaman: ", tanggal_pinjam)

        jumlah = getTotal(data,current_idx[i])
        print("Jumlah: ", jumlah)
        print("")

def getDataLen (data):
    x = 0
    count = 0
    flag = True
    while flag:
        if (x < len(data)-1):
            x += 1
            count += 1
        else:
            flag = False
    return count

def findLowest (data, length):
    date_column = []
    for i in range (1, length+1):
        date_column.append(data[i][3])
        date_column.sort(key=lambda date: datetime.datetime.strptime(date, "%d-%b-%y"))
        date_column.reverse()
    
    idx_list = []
    flag = True
    j = 1
    k = 0
    while flag:
        if (date_column[k] == data[j][3]) and (k < (len(date_column))):
            idx_list.append(j)
            k += 1
            j = 0
            if len(idx_list) == len(date_column):
                flag = False
        else: 
            j += 1
    return idx_list
    
def getID (data,x):
    return data[x][0]

def getPeminjam (data,x):
    return data[x][1]

def getGadget (data,x):
    return data[x][2]

def getDate (data,x):
    return data[x][3]

def getTotal (data,x):
    return data[x][4]