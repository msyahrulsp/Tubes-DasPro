def searchByID(data,id):
    for x in data:
        if x[0] == id : return True
    return False 

def searchByRarity(data,request):
    state = True
    print("\nHasil pencarian: \n")
    for x in data:
        newdata = x
        if newdata[4] == request : 
            state = False
            print(f'Nama            : {newdata[1]} ')
            print(f'deskripsi       : {newdata[2]} ')
            print(f'jumlah          : {newdata[3]} ')
            print(f'rarity          : {newdata[4]} ')
            print(f'tahun ditemukan : {newdata[5]} \n')
    if state :
        print('Tidak ada gadget ditemukan\n')

#ex pengunaan : 
'''
searchByRarity(consumable,'S')
'''

def searchByYear(data,request,type):
    state = True
    print("\nHasil pencarian: \n")
    for x in data:
        newdata = x
        if type == '=':
            if int(newdata[5]) == request : 
                state = False
                print(f'Nama            : {newdata[1]} ')
                print(f'deskripsi       : {newdata[2]} ')
                print(f'jumlah          : {newdata[3]} ')
                print(f'rarity          : {newdata[4]} ')
                print(f'tahun ditemukan : {newdata[5]} \n')  
        if type == '>' :
            if int(newdata[5]) > request : 
                state = False
                print(f'Nama            : {newdata[1]} ')
                print(f'deskripsi       : {newdata[2]} ')
                print(f'jumlah          : {newdata[3]} ')
                print(f'rarity          : {newdata[4]} ')
                print(f'tahun ditemukan : {newdata[5]} \n')      
        if type == '<':
            if int(newdata[5]) < request :
                state = False
                print(f'Nama            : {newdata[1]} ')
                print(f'deskripsi       : {newdata[2]} ')
                print(f'jumlah          : {newdata[3]} ')
                print(f'rarity          : {newdata[4]} ')
                print(f'tahun ditemukan : {newdata[5]} \n')
    if state :
        print('Tidak ada gadget ditemukan\n')

# ex penggunaan : 
'''
searchByYear(gadget,2020,'=')
'''
