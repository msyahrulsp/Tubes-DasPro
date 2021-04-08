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
    fieldnames = ['id','username','nama','alamat','password','role']
    nama = input('Masukan nama : ')
    username = input('Masukan username : ')
    if isUsernameUnique(username,mydata) is True: return '0' # if the return value, that means that the username is not unique, thus we will not continue the registration
    password = hash.Hash(input('Masukan password : '))
    alamat = input('Masukan alamat : ')
    data.appendData('Data/user.csv',fieldnames,{'id':len(mydata),'username':username,'nama':nama,'alamat': alamat,'password':password,'role':0})

register()


