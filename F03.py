from Modules import split,data

def searchByRarity(data,request):
    state = True
    for i in data[1:]:
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
contoh = data.loadData('Data/gadget.csv')
searchByRarity(contoh,'S')
'''
