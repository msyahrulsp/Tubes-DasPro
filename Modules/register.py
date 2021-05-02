from Util import hash

'''
fungsi ini mengembalikan true jika username yang diberikan memang unique
'''

def isUsernameUnique(username,data): 
    for x in data:
        if x[1] == username: return False
    return True



    # { I.S. : Menerima input data user
    # { F.S. : Mendaftarkan user pada sistem kami }

    # KAMUS
    #users,data : array
    # username,password,alamat,uid : string

    # ALGORITMA
    #data : array of user

def register(data): 
    mydata = data[1:]

    if len(mydata)  == 0:
        uid = '1'
    else:     
        uid = str(int(mydata[len(mydata)-1][0]) + 1) # Ngambil Index dari last elemen (should be otomatis unique)

    nama = input('Masukan nama : ').title() # Awal huruf tiap kata besar
    username = input('Masukan username : ')

    if isUsernameUnique(username,mydata) is False: 
        print('Username sudah ada di dalam database, mohon untuk login menggunakan username tersebut')
        return ['0'] # if the return value, that means that the username is not unique, thus we will not continue the registration
        # Returnnya array biar gampang dijadiin notasi algoritmik

    password = hash.Hash(input('Masukan password : '))
    alamat = input('Masukan alamat : ')
    print(f'\nUser {username} telah berhasil register ke dalam Kantong Ajaib')
    input('Tekan enter untuk melanjutkan')
    return([uid, username, nama, alamat, password, "user"])