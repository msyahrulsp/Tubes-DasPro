import datetime

def gadget_ret_hist (data):
    # { I.S. : Menerima data dari file csv gadget_return_history dalam bentuk array }
    # { F.S. : Mencetak data - data dalam file csv gadget_return_history yang sudah diurutkan menurut tanggal }

    # KAMUS
    # date_sorted, idx_list : array
    # currentStart, currentEnd : integer
    # userPref : string
    # flagMain : boolean

    # ALGORITMA
    if (len(data)) == 1:
        print("Data masih kosong!")
    else:
        date_sorted = sortDate(data)            # mengembalikan array dengan tanggal terurut dari besar ke kecil
        idx_list = findIdx(data, date_sorted)   # mengembalikan array dengan indeks yang sesuai dengan tanggal
        currentStart = 0                        # start awal loop selalu mulai dari 0
        if ((len(data)) < 6):                   # jika panjang data < 6, maka currentEnd harus mengikuti panjang data kurang 1
            currentEnd = len(idx_list)
        else:
            currentEnd = 5                      # jika panjang data > 6 (artinya ada lebih data), currentEnd dimulai dari 5
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
                    if (currentStart + 5) > (len(idx_list)):# jika nilai currentStart + 5 > panjang idx_list, artinya sisa data tidak lagi ada 5, sehingga currentEnd menjadi panjang idx_list
                        currentEnd = len(idx_list)
                    else:                                   # jika nilai currentStart + 5 <= panjang idx_list, artinya indeks end akan ditambah 5, karena data masih lebih dari 5
                        currentEnd = currentEnd + 5         
                output(currentStart,currentEnd,data,idx_list)

def output (currentStart,currentEnd,data,idx_list):
    # { I.S. : Menerima input currentStart, currentEnd, data, dan idx_list }
    # { F.S. : Mengambil 5 data dari array yang sudah terurut dengan start dan end tertentu dan mencetaknya } 

    # KAMUS
    # idx, id_peminjam, id_gadget, tanggal_pinjam, jumlah : string
    # i : integer
    # data : array

    # ALGORITMA
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
    # { I.S. : Menerima input data }
    # { F.S. : Mengisi sebuah array baru 'date_sorted' yang berisi tanggal terurut } 

    # KAMUS
    # date_sorted : array
    # i : integer
    # data : array

    # ALGORITMA
    date_sorted = []
    for i in range (1, len(data)):
        date_sorted.append(data[i][3])
        date_sorted.sort(key=lambda date: datetime.datetime.strptime(date, '%d/%m/%Y')) # pengurutan dilakukan dari tanggal yang paling kecil
        date_sorted.reverse()   # membalikkan urutan array 'date_sorted'
    return date_sorted
    
def findIdx (data, date):
    # { I.S. : Menerima input data dan array date }
    # { F.S. : Mencari indeks dari tanggal tertentu dan memasukkannya ke dalam array idx_list }

    # KAMUS
    # idx_list, date, data : array
    # i, j, k : integer
    # flag : boolean

    # ALGORITMA
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
    # { I.S. : Menerima input data dan integer x }
    # { F.S. : Mengambil data di baris x dan kolom 1 }

    # KAMUS
    # data : array
    # x : integer

    # ALGORITMA
    return data[x][0]

def getPeminjam (data,x):
    # { I.S. : Menerima input data dan integer x }
    # { F.S. : Mengambil data di baris x dan kolom 2 }

    # KAMUS
    # data : array
    # x : integer

    # ALGORITMA
    return data[x][1]

def getGadget (data,x):
    # { I.S. : Menerima input data dan integer x }
    # { F.S. : Mengambil data di baris x dan kolom 3 }

    # KAMUS
    # data : array
    # x : integer

    # ALGORITMA
    return data[x][2]

def getDate (data,x):
    # { I.S. : Menerima input data dan integer x }
    # { F.S. : Mengambil data di baris x dan kolom 4 }

    # KAMUS
    # data : array
    # x : integer

    # ALGORITMA
    return data[x][3]