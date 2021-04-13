from Util import hash

def isUsernameUnique(username,data): 
    for x in data:
        if x[1] == username: return True
    return False

def register(data): 
    mydata = data
    uid = int(mydata[len(mydata)-1][0]) + 1 # Ngambil Index dari last elemen (should be otomatis unique)
    nama = input('Masukan nama : ').title() # Awal huruf tiap kata besar
    username = input('Masukan username : ')

    if isUsernameUnique(username,mydata) is True: 
        print('Username sudah ada di dalam database, mohon untuk login menggunakan username tersebut')
        return ['0'] # if the return value, that means that the username is not unique, thus we will not continue the registration
        # Returnnya array biar gampang dijadiin notasi algoritmik

    password = hash.Hash(input('Masukan password : '))
    alamat = input('Masukan alamat : ')
    # mydata.append(f'{uid};{username};{nama};{alamat};{password};user')
    print(f'User {username} telah berhasil register ke dalam Kantong Ajaib')
    return([uid, username, nama, alamat, password, "user"])
    # data.saveData('Data/user.csv',''.join(mydata)) # Gk autosave