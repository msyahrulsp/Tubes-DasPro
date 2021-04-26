import datetime

def gadget_ret_hist (data):
    date_sorted = sortDate(data)            # mengembalikan array dengan tanggal terurut dari besar ke kecil
    idx_list = findIdx(data, date_sorted)   # mengembalikan array dengan indeks yang sesuai dengan tanggal
    currentStart = 0
    currentEnd = len(idx_list)
    output(currentStart,currentEnd,data,idx_list)

    flagMain = True
    while flagMain:
        userPref = input("Apakah anda ingin melihat 5 data lagi? (y/n) ")
        if userPref == "n":
            flagMain = False
        else:
            if (currentStart >= (len(idx_list)-1)):     # indeks start awal lebih atau sama dengan panjang array 'idx_list'-1
                print("Data sudah habis!")              # data akan habis jika syarat tersebut terpenuhi
                flagMain = False
            else:
                currentStart += 5                       # indeks start akan selalu ditambah 5

            if (currentEnd >= (len(idx_list)-1)):       # indeks end akhir lebih atau sama dengan panjang data 'idx_list'-1
                print("Data sudah habis!")              # data akan habis jika syarat tersebut terpenuhi
                flagMain = False
            else:  
                currentEnd = currentEnd + (len(idx_list) - currentEnd)      # indeks end akan selalu ditambah selisih panjang array dengan awalnya
            output(currentStart,currentEnd,data,idx_list)

def output (currentStart,currentEnd,data,idx_list):
    # Mengambil 5 data dari array yang sudah terurut dengan start dan end tertentu
    for i in range (currentStart,currentEnd):
        idx = getID(data,idx_list[i])
        print("ID Peminjaman: ", idx)

        id_peminjam = getPeminjam(data,idx_list[i])
        print("Nama Pengambil: ", id_peminjam)

        id_gadget = getGadget(data,idx_list[i])
        print("Nama Gadget: ", id_gadget)

        tanggal_pinjam = getDate(data,idx_list[i])
        print("Tanggal Peminjaman: ", tanggal_pinjam)
        print("")

def sortDate (data):
    # Mengisi sebuah array baru 'date_sorted' yang berisi tanggal terurut
    date_sorted = []
    for i in range (1, len(data)):
        date_sorted.append(data[i][3])
        date_sorted.sort(key=lambda date: datetime.datetime.strptime(date, '%d/%m/%Y')) # pengurutan dilakukan dari tanggal yang paling kecil
        date_sorted.reverse()   # membalikkan urutan array 'date_sorted'
    return date_sorted
    
def findIdx (data, date):
    # Mencari indeks dari tanggal tertentu
    idx_list = []
    flag = True
    j = 1
    k = 0
    while flag:
        if (date[k] == data[j][3]) and (k < (len(date))):   # jika tanggal pada array 'date' sama dengan tanggal pada array 'data' dan nilai k < panjang array 'date'
            idx_list.append(j)
            k += 1
            j = 0
            if len(idx_list) == len(date):  # jika panjang array 'idx_list' sudah sepanjang dengan array 'date', berarti semua data sudah diproses dan dicari indeksnya
                flag = False
        else: 
            j += 1
    return idx_list
    
def getID (data,x):
    # mengambil data di baris x dan kolom 0
    return data[x][0]

def getPeminjam (data,x):
    # mengambil data di baris x dan kolom 1
    return data[x][1]

def getGadget (data,x):
    # mengambil data di baris x dan kolom 2
    return data[x][2]

def getDate (data,x):
    # mengambil data di baris x dan kolom 3
    return data[x][3]