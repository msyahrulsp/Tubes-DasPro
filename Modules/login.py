from Util import hash

# if error = 0, it means the username is not registered in the database 
# if error = 1, it means that the password is incorrect

    # { I.S. : Menerima input data user
    # { F.S. : Menghasilkan user session jike ternyata user memang terdaftar pada sistem kami }

    # KAMUS
    #users,data : array
    # username,password : string

    # ALGORITMA
    
def login(data):
    users = data[1:]
    username = input('Masukan username : ')
    for user in users:
        if username == user[1] :
            if hash.Hash(input('Masukan password : ')) == user[4]:
                print(f'\nHallo {user[2]}! Selamat datang di Kantong Ajaib')
                return (user[0], user[5]) # ID, Role
            return ('1', '1') # Kenapa pake tuple juga?? biar gampang di notasi algoritmiknya
    return ('0', '0')