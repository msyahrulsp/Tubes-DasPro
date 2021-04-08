from Modules import data,hash,split

# if error = 0, it means the username is not registered in the database 
# if error = 1, it means that the password is incorrect


def login():
    users = ''.join(str(p) for p in data.loadData('Data/user.csv'))
    #print(users)
    #print(users)
    username = input("Masukan Username : ")
    if username not in users : return '0'
    password = hash.Hash(input("Masukan Password : "))
    if password not in users : return '1'
    return username
    

