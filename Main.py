import loadData,register,login

# datas : array of [0...<3]
# datas[0] = user's datas
# datas[1] = consumable datas
# datas[2] = gadget datas

#usersession store user's id and user's name // debatable

def main(): 
    return

if __name__ == '__main__':
    usersession = login.login()
    datas = loadData.LoadData(usersession)
    main()
    