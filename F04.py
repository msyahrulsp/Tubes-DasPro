from Modules import split,data

def searchByYear(data,request,type):
    state = True
    for i in data[1:]:
        newdata = split.split(i)
        if type == '=':
            state = False
            if int(newdata[5]) == request : 
                print(f'Nama            : {newdata[1]} ')
                print(f'deskripsi       : {newdata[2]} ')
                print(f'jumlah          : {newdata[3]} ')
                print(f'rarity          : {newdata[4]} ')
                print(f'tahun ditemukan : {newdata[5]} ')  
        if type == '>' :
            state = False
            if int(newdata[5]) > request : 
                print(f'Nama            : {newdata[1]} ')
                print(f'deskripsi       : {newdata[2]} ')
                print(f'jumlah          : {newdata[3]} ')
                print(f'rarity          : {newdata[4]} ')
                print(f'tahun ditemukan : {newdata[5]} ')      
        if type == '<':
            state = False
            if int(newdata[5]) < request : 
                print(f'Nama            : {newdata[1]} ')
                print(f'deskripsi       : {newdata[2]} ')
                print(f'jumlah          : {newdata[3]} ')
                print(f'rarity          : {newdata[4]} ')
                print(f'tahun ditemukan : {newdata[5]} ')
    if state :
        print('Tidak ada gadget ditemukan')


# ex penggunaan : 
'''
contoh = data.loadData('Data/gadget.csv')
searchByYear(contoh,2020,'=')
'''