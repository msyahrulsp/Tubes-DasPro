from time import time, sleep

def getAvaRarity(data):
    temp = []
    for i in range(len(data)):
        if data[i][4] not in temp:
            temp.append(data[i][4])
    return temp

def genChance(num, rarity, listChance):
    multiplier = 12
    idx = 0
    if rarity == "B":
        multiplier = 15
        idx = 1
    if rarity == "A":
        multiplier = 18
        idx = 2
    if rarity == "S":
        multiplier = 20
        idx = 3

    chance = ((num**2)*100)/((num**2)+(multiplier*35)*(num+100))
    if idx != 3:
        listChance[idx+1] += chance # Rarity lebih tinggi
    listChance[idx] += (3/2) * chance # Rarity sendiri
    return listChance

def random(modulus):
    seed = round(time())
    a = 244123
    b = round(time()) // 12123
    temp = (a * seed + b) % modulus
    return temp

def genRarity(chance):
    rarity = ["C", "B", "A", "S"]

    rand = random(100.00)

    for i in range(3, -1, -1):
        if rand >= 0 and rand <= chance[i]:
            return rarity[i]
        sleep(1)
        rand = random(100.00)

    return "Failed"

def getItem(data, rarity):
    temp = []
    for i in range(len(data)):
        if data[i][4] == rarity:
            temp.append([data[i][0], data[i][1]])

    modulus = len(temp)
    rand = random(modulus)

    return temp[rand]

def checkInvent(data, userid):
    for i in range(len(data)):
        if data[i][3] == userid:
            return True
    return False