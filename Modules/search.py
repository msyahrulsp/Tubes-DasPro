from Util import split
# from Modules import split,data

def searchByID(data,id):
    for i in data:
        if split.split(i)[0] == id : return True
    return False 

def searchByRarity(data,request):
    state = True
    for i in data:
        newdata = split.split(i)
        if newdata[4] == request : 
            state = False
            print(f'Nama            : {newdata[1]} ')
            print(f'deskripsi       : {newdata[2]} ')
            print(f'jumlah          : {newdata[3]} ')
            print(f'rarity          : {newdata[4]} ')
            print(f'tahun ditemukan : {newdata[5]} ')
    if state :
        print('Tidak ada gadget ditemukan')

#ex pengunaan : 
'''
searchByRarity(consumable,'S')
'''

def searchByYear(data,request,type):
    state = True
    for i in data:
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
searchByYear(gadget,2020,'=')
'''
