from Modules import data,hash

def login():
    users = data.loadData('Data/user.csv')
    print(users)
    

login()