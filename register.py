from Modules import hash,data,split


#role

# 0 = user biasa
# >40 administrator

#set unique id to id, but how????

#idenya sih len(data) = id si user yg baru gabung
# buat cek is username is unique, ntar bikin fungsi baru

def isUsernameUnique(username,data): 
    for i in data:
        if split.split(i)[1] == username: return True
    return False

def register(): 
    mydata = data.loadData('Data/user.csv')
    uid = len(mydata)
    nama = input('Masukan nama : ')
    username = input('Masukan username : ')
    if isUsernameUnique(username,mydata) is True: return '0' # if the return value, that means that the username is not unique, thus we will not continue the registration
    password = hash.Hash(input('Masukan password : '))
    alamat = input('Masukan alamat : ')
    mydata.append(f'{uid};{username};{nama};{alamat};{password};0\n')
    print(mydata)
    data.saveData('Data/user.csv',''.join(mydata))
 
register()