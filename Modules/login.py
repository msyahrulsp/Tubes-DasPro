from Util import hash

# if error = 0, it means the username is not registered in the database 
# if error = 1, it means that the password is incorrect

# need to fix the login ssystem, it should return the user's id


def login(data):
    users = data#''.join(data.loadData('Data/user.csv'))
    username = input('Username : ')
    for user in users:
        if username == user[1] :
            if hash.Hash(input('Password : ')) == user[4]:
                print(f'Hallo {user[1]}! Selamat datang di Kantong Ajaib')
                return (user[0], user[5])
            return ('1', '1') # Kenapa pake tuple juga?? biar gampang di notasi algoritmiknya
    return ('0', '0')
    
