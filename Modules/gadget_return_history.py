import datetime

def gadget_ret_hist (hist, user, gadget):
    # { I.S. : Menerima data dari file csv gadget_return_history, user, dan gadget dalam bentuk array }
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
        output(currentStart,currentEnd,hist,user,gadget,idx_list)

        flagMain = True
        while flagMain:
            userPref = input("Apakah anda ingin melihat 5 data lagi? (y/n) ")
            if userPref == "n":
                flagMain = False
            else:
                if (currentStart >= (len(idx_list))):     # indeks start awal lebih atau sama dengan panjang array 'idx_list'
                    print("Data sudah habis!")              # data akan habis jika syarat tersebut terpenuhi
                    flagMain = False
                else:
                    currentStart += 5                       # indeks start akan selalu ditambah 5

                if (currentEnd >= (len(idx_list))):       # indeks end akhir lebih atau sama dengan panjang data 'idx_list'
                    print("Data sudah habis!")              # data akan habis jika syarat tersebut terpenuhi
                    flagMain = False
                else:  
                    if (currentStart + 5) > (len(idx_list)):# jika nilai currentStart + 5 > panjang idx_list, artinya sisa data tidak lagi ada 5, sehingga currentEnd menjadi panjang idx_list
                        currentEnd = len(idx_list)
                    else:                                   # jika nilai currentStart + 5 <= panjang idx_list, artinya indeks end akan ditambah 5, karena data masih lebih dari 5
                        currentEnd = currentEnd + 5         
                output(currentStart,currentEnd,hist,user,gadget,idx_list)

def output (currentStart,currentEnd,hist,user,gadget,idx_list):
    # { I.S. : Menerima input currentStart, currentEnd, hist, user, gadget dan idx_list }
    # { F.S. : Mengambil 5 data dari array yang sudah terurut dengan start dan end tertentu dan mencetaknya } 

    # KAMUS
    # idx, id_gadget, nama_gadget, tanggal_pinjam, jumlah : string
    # i, id_peminjam : integer
    # hist : array

    # ALGORITMA
    for i in range (currentStart,currentEnd):
        idx = getID(hist,idx_list[i])
        print("ID Pengembalian: ", idx)

        id_pengambil = int(getPengambil(hist,idx_list[i]))
        nama_pengambil = user[id_pengambil][2]
        print("Nama Pengambil: ", nama_pengambil)

        tanggal_kembali = getDate(hist,idx_list[i])
        print("Tanggal Pengembalian: ", tanggal_kembali)

        jumlah = getTotal(hist,idx_list[i])
        print("Jumlah: ", jumlah)
        print("")

def sortDate (hist):
    # { I.S. : Menerima input data }
    # { F.S. : Mengisi sebuah array baru 'date_sorted' yang berisi tanggal terurut } 

    # KAMUS
    # date_sorted, hist : array
    # i : integer

    # ALGORITMA
    date_sorted = []
    for i in range (1, len(hist)):
        date_sorted.append(hist[i][2])
        date_sorted.sort(key=lambda date: datetime.datetime.strptime(date, '%d/%m/%Y')) # pengurutan dilakukan dari tanggal yang paling kecil
        date_sorted.reverse()   # membalikkan urutan array 'date_sorted'
    return date_sorted
    
def findIdx (hist, date):
    # { I.S. : Menerima input data dan array date }
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
        if (date[k] == hist[j][2]) and (k < (len(date))):   # jika tanggal pada array 'date' sama dengan tanggal pada array 'hist' dan nilai k < panjang array 'date'
            idx_list.append(j)
            k += 1
            j = 0
            if len(idx_list) == len(date):  # jika panjang array 'idx_list' sudah sepanjang dengan array 'date', berarti semua hist sudah diproses dan dicari indeksnya
                flag = False
        else: 
            j += 1
    return idx_list
    
def getID (hist,x):
    # { I.S. : Menerima input data dan integer x }
    # { F.S. : Mengambil data di baris x dan kolom 1 }

    # KAMUS
    # data : array
    # x : integer

    # ALGORITMA
    return hist[x][0]

def getPengambil (hist,x):
    # { I.S. : Menerima input data dan integer x }
    # { F.S. : Mengambil data di baris x dan kolom 2 }

    # KAMUS
    # data : array
    # x : integer

    # ALGORITMA
    return hist[x][1]

def getDate (hist,x):
    # { I.S. : Menerima input data dan integer x }
    # { F.S. : Mengambil data di baris x dan kolom 3 }

    # KAMUS
    # data : array
    # x : integer

    # ALGORITMA
    return hist[x][2]

def getTotal (hist,x):
    # { I.S. : Menerima input data dan integer x }
    # { F.S. : Mengambil data di baris x dan kolom 4 }

    # KAMUS
    # data : array
    # x : integer

    # ALGORITMA
    return hist[x][3]