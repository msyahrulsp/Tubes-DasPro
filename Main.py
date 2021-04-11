import loadData,register,login
import os,sys
import argparse


# datas : array of [0...<3]
# datas[0] = user's datas aka the user's id
# datas[1] = consumable datas
# datas[2] = gadget datas

#usersession store user's id and user's name // debatable
def help(): 
    print('a')
    input('please enter to continue')

def main(data): 
    print('User Id : ' + data[0])
    print(data[2])
    return

if __name__ == '__main__':
    # si itunya, gajelas emg
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", help="the folder name")
    args = parser.parse_args()
    print(args.folder) #nama foldernya in string
    # jgn diganggu gugat, batas suci
    state = True
    while state :
        print("""
0   - help
1   - login
2   - register
99  - exit
        """)
        pilihan = int(input('Pilihan anda : '))
        if pilihan == 0:
            help()
        elif pilihan == 2:
            register.register()
        elif pilihan == 1:
            usersession = login.login()
            if usersession == '0' :
                print("Your username is incorrent") 
            elif usersession == '1':
                print("Your password is incorrect")
            else :
                main(loadData.LoadData(usersession,args.folder))
        elif pilihan == 99:
            state = False
        else : 
            print('Pilihan tidak tersedia')
            