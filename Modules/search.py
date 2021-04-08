import split

def searchByID(data,id):
    for i in data:
        if split.split(i)[0] == id : return True
    return False 