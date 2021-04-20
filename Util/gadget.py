from Util.validasi import getId

def checkGadget(datah, idg, userid): # Fungsi buat ngecek user lagi minjem gadget atau enggak
    for i in range(len(datah)):
        if (datah[i][1] == userid) and (datah[i][2] == idg):
            jmlh = datah[i][4]
            jmlh_r = datah[i][5]
            if (jmlh != jmlh_r):
                return False
    return True

def userGadget(datah, userid):
    temp = []

    for i in range(1, len(datah)):
        if (datah[i][1] == userid): 
            if (datah[i][4] != datah[i][5]):
                temp.append(datah[i])

    return temp