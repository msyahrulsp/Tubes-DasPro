from Modules import data

# datas : array of [0...<3]
# datas[0] = user's datas
# datas[1] = consumable datas
# datas[2] = gadget datas

#usersession store user's id and user's name // debatable

def LoadData(usersession): 
    return [usersession,data.loadData('Data/consumable.csv'),data.loadData('Data/gadget.csv')]



