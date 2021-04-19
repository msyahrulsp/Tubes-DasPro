from Util.validasi import getId

def checkGadget(invent, idg, userid): # Fungsi buat ngecek user lagi minjem gadget atau enggak
    for i in range(len(invent)):
        if (invent[i][0] == userid) and (invent[i][2] == idg):
            return False
    return True

def userGadget(userid, data):
    temp = []

    idx = getId(data, userid)

    for i in range(1, len(data)):
        for i in range(1, len(data)):
            if data[i][1] == userid:
                data[i].append(i) # Nambah index buat inget kemambilnya di index keberapa di inventory.csv
                data[i].append(idx) # Nambah index gadget di gadget.csv
                temp.append(data[i])

    return temp