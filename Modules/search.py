def searchByID(data,id):
    for x in data:
        if x[0] == id : return True
    return False 

def searchByRarity(data,request):
    state = True
    print("\nHasil pencarian: ")
    for newdata in data[1:]:
        if newdata[4] == request : 

            state = False
            print(f'\nNama            : {newdata[1]} ')
            print(f'Deskripsi       : {newdata[2]} ')
            print(f'Jumlah          : {newdata[3]} ')
            print(f'Rarity          : {newdata[4]} ')
            print(f'Tahun Ditemukan : {newdata[5]} ')
    if state :
        print('Tidak ada gadget ditemukan\n')

#ex pengunaan : 
'''
searchByRarity(consumable,'S')
'''
def searchByYear(data,request,type): #data = datanya yg mau di search, request = tahun yang diperlukan, type = tipenya
    state = True
    print("\nHasil pencarian: ")
    try :
        for newdata in data[1:]:
            if eval(f'{int(newdata[5])} {type} {request}'):
                state = False
                print(f'\nNama            : {newdata[1]} ')
                print(f'Deskripsi       : {newdata[2]} ')
                print(f'Jumlah          : {newdata[3]} ')
                print(f'Rarity          : {newdata[4]} ')
                print(f'Tahun Ditemukan : {newdata[5]} ')
        if state :
            print('Tidak ada gadget ditemukan\n')
    except:
        print('Tidak ada gadget ditemukan\n')

# ex penggunaan : 
'''
searchByYear(gadget,2020,'=')
'''
