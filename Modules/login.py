from Util import hash,split

# if error = 0, it means the username is not registered in the database 
# if error = 1, it means that the password is incorrect

# need to fix the login ssystem, it should return the user's id


def login(data):
    users = data#''.join(data.loadData('Data/user.csv'))
    username = input('Username : ')
    for i in users: 
        userdata = split.split(i)
        if username == userdata[1] :
            if hash.Hash(input('Password : ')) == userdata[4]:
                print(f'Hallo {userdata[1]}! Selamat datang di Kantong Ajaib')
                return userdata[5]
            return '1'
    return '0'
    
