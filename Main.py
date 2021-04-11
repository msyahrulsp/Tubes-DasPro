import loadData,register,login

# datas : array of [0...<3]
# datas[0] = user's datas
# datas[1] = consumable datas
# datas[2] = gadget datas

#usersession store user's id and user's name // debatable

def main(data): 
    print(data[0])
    return

if __name__ == '__main__':
    usersession = login.login()
    if usersession == '0' :
        print("Your username is inccorent") 
    elif usersession == '1':
        print("Your password is incorrect")
    else :
        main(loadData.LoadData(usersession))
    