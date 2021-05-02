import datetime

def consum_hist (hist, user, consum):
    # { I.S. : Menerima data dari file csv consumable_history, user, dan consumable dalam bentuk array }
    # { F.S. : Mencetak data - data yang diminta dan menanyakan apabila ingin menampilkan 5 data lagi }

    # KAMUS
    # date_sorted, idx_list : array
    # currentStart, currentEnd : integer
    # userPref : string
    # flagMain : boolean

    # ALGORITMA
    if (len(hist)) == 1:
        print("Data masih kosong!")
    else:
        date_sorted = sortDate(hist)            # mengembalikan array dengan tanggal terurut dari besar ke kecil
        idx_list = findIdx(hist, date_sorted)   # mengembalikan array dengan indeks yang sesuai dengan tanggal
        currentStart = 0                        # start awal loop selalu mulai dari 0
        if ((len(hist)) < 6):                   # jika panjang hist < 6, maka currentEnd harus mengikuti panjang idx_list
            currentEnd = len(idx_list)
        else:
            currentEnd = 5                      # jika panjang hist > 6 (artinya ada lebih data), currentEnd dimulai dari 5
        output(currentStart,currentEnd,hist,user,consum,idx_list)

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
                output(currentStart,currentEnd,hist,user,consum,idx_list)

def output (currentStart,currentEnd,hist,user,consum,idx_list):
    # { I.S. : Menerima input currentStart, currentEnd, hist, user, consum, dan idx_list }
    # { F.S. : Mengambil 5 data dari array yang sudah terurut dengan start dan end tertentu dan mencetaknya } 

    # KAMUS
    # idx, nama_pengambil, id_consumable, nama_consumable, tanggal_pinjam, jumlah : string
    # i, id_pengambil : integer
    # hist, user, consum : array

    # ALGORITMA
    for i in range (currentStart,currentEnd):
        idx = getID(hist,idx_list[i])
        print("ID Pengambilan: ", idx)

        id_pengambil = int(getPengambil(hist,idx_list[i]))
        nama_pengambil = user[id_pengambil][2]
        print("Nama Pengambil: ", nama_pengambil)

        id_consumable = getConsumable(hist,idx_list[i])
        nama_consumable = findConsumable(id_consumable, consum)
        print("Nama Consumable: ", id_consumable)

        tanggal_pinjam = getDate(hist,idx_list[i])
        print("Tanggal Pengambilan: ", tanggal_pinjam)

        jumlah = getTotal(hist,idx_list[i])
        print("Jumlah: ", jumlah)
        print("")

def sortDate (hist):
    # { I.S. : Menerima input hist }
    # { F.S. : Mengisi sebuah array baru 'date_sorted' yang berisi tanggal terurut } 

    # KAMUS
    # date_sorted, hist : array
    # i : integer

    # ALGORITMA
    date_sorted = []
    for i in range (1, len(hist)):
        date_sorted.append(hist[i][3])
        date_sorted.sort(key=lambda date: datetime.datetime.strptime(date, '%d/%m/%Y')) # pengurutan dilakukan dari tanggal yang paling kecil
        date_sorted.reverse()   # membalikkan urutan array 'date_sorted'
    return date_sorted
    
def findIdx (hist, date):
    # { I.S. : Menerima input hist dan array date }
    # { F.S. : Mencari indeks dari tanggal tertentu dan memasukkannya ke dalam array idx_list }

    # KAMUS
    # idx_list, date, hist : array
    # i, j, k : integer
    # flag : boolean

    # ALGORITMA
    idx_list = []
    flag = True
    j = 1
    k = 0
    while flag:
        if (date[k] == hist[j][3]) and (k < (len(date))):   # jika tanggal pada array 'date' sama dengan tanggal pada array 'hist' dan nilai k < panjang array 'date'
            idx_list.append(j)
            k += 1
            j = 0
            if len(idx_list) == len(date):  # jika panjang array 'idx_list' sudah sepanjang dengan array 'date', berarti semua data sudah diproses dan dicari indeksnya
                flag = False
        else: 
            j += 1
    return idx_list

def findConsumable (idx, consum):
    # { I.S. : Menerima input idx dan array consum }
    # { F.S. : Mengembalikan data di array consum sesuai idx tertentu }

    # KAMUS
    # consum : array
    # idx : string
    # flag : boolean
    # i : integer

    # ALGORITMA
    flag = True
    i = 1
    while flag:
        if consum[i][0] == idx:
            return consum[i][1]
            flag = False
        else:
            i += 1
    
def getID (hist,x):
    # { I.S. : Menerima input hist dan integer x }
    # { F.S. : Mengambil hist di baris x dan kolom 1 }

    # KAMUS
    # hist : array
    # x : integer

    # ALGORITMA
    return hist[x][0]

def getPengambil (hist,x):
    # { I.S. : Menerima input hist dan integer x }
    # { F.S. : Mengambil hist di baris x dan kolom 2 }

    # KAMUS
    # hist : array
    # x : integer

    # ALGORITMA
    return hist[x][1]

def getConsumable (hist,x):
    # { I.S. : Menerima input hist dan integer x }
    # { F.S. : Mengambil hist di baris x dan kolom 3 }

    # KAMUS
    # hist : array
    # x : integer

    # ALGORITMA
    return hist[x][2]

def getDate (hist,x):
    # { I.S. : Menerima input hist dan integer x }
    # { F.S. : Mengambil hist di baris x dan kolom 4 }

    # KAMUS
    # hist : array
    # x : integer

    # ALGORITMA
    return hist[x][3]

def getTotal (hist,x):
    # { I.S. : Menerima input hist dan integer x }
    # { F.S. : Mengambil hist di baris x dan kolom 5 }

    # KAMUS
    # hist : array
    # x : integer

    # ALGORITMA
    return hist[x][4]