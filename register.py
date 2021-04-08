from Modules import hash,data

#role

# 0 = user biasa
# >40 administrator

#set unique id to id, but how????

#idenya sih len(data) = id si user yg baru gabung
def register(): 
    banyakdata = data.loadData('Data/user.csv')
    fieldnames = ['id','username','nama','alamat','password','role']
    nama = input('Masukan nama : ')
    username = input('Masukan username : ')
    password = hash.Hash(input('Masukan password : '))
    alamat = input('Masukan alamat : ')
    data.appendData('Data/user.csv',fieldnames,{'id':len(banyakdata),'username':username,'nama':nama,'alamat': alamat,'password':password,'role':0})

register()