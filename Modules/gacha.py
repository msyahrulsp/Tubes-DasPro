from time import sleep
from datetime import datetime
from Util.gacha import checkInvent, genRarity, getAvaRarity, genChance, getItem

def gacha(invent, datac, datah, userid):
    # { I.S. : Menerima input berupa data inventory, consumable, history consumable dan user id}
    # { F.S. : Menghasilkan item dengan rarity baru (jika beruntung) dan menambahkan item tersebut ke inventory user dan data history}

    # KAMUS
    # avaRarity, rare : array of string
    # chance, tempidx : array of integer
    # item : array of (qty, idx)
    # qty, idx, count, opt, qty : integer
    # confirm, half, refund : boolean
    # again, date, rarity, idh : string

    # ALGORITMA

    avaRarity = getAvaRarity(datac) # ngecek rarity apa aja yang ada di cons
    if len(avaRarity) == 0:
        print("\nTidak ada consumable pada stock")

    elif not checkInvent(invent, userid):
        print("\nKamu belum meminta consumable apapun")

    else:

        chance = [0, 0, 0, 0] # C B A S
        item = [] # Holder qty sama idx
        confirm = True

        # Nge loop terus sampe again = n
        # atau sampe gk punya lagi consumable di inventory
        while confirm:
            print("\n==========INVENTORY==========")
            count = 0
            tempidx = []
            for i in range(1, len(invent)):
                if invent[i][1][0] == "C" and invent[i][3] == userid and invent[i][5] != '0':
                    count += 1
                    print("%d. %s (Rarity %s) (%s)" % (count, invent[i][2], invent[i][4], invent[i][5]))
                    tempidx.append(i)

            if count == 0:
                print("Tidak ada consumable yang bisa dicombine")
                confirm = False
                
            else:

                print("=============================")
                opt = int(input("\nPilih consumable yang mau digunakan: "))

                while (opt < 1) or (opt > len(tempidx)):
                    print("\nInput invalid")
                    opt = int(input("\nPilih consumable yang mau digunakan: "))

                idx = tempidx[opt-1]

                qty = int(input("Jumlah yang digunakan: "))
                while (qty < 0) or (qty > int(invent[idx][5])):
                    print("\nInput invalid")
                    qty = int(input("\nJumlah yang digunakan: "))

                print("\n%s (x%d) ditambahkan!\n" % (invent[idx][2], qty))

                # Ngurangin sementara, why?
                # Safecase buat rarity yang didapat dari gacha gk ada di consumable
                invent[idx][5] = str(int(invent[idx][5]) - qty)

                # Index di inventory, qty dari input
                item.append([idx, qty])

                chance = genChance(qty, invent[idx][4], chance) # Generate chance
                rare = ["C", "B", "A", "S"]
                for i in range(4):
                    print("Chance mendapatkan Rarity %s = %.2f%%" % (rare[i], chance[i]))

                again = input("\nTambahkan item lagi? (y/n) : ").lower()
                while (again != "y") and (again != "n"):
                    print("\nInput invalid")
                    again = input("Tambahakan item lagi? (y/n) : ").lower()

                if again == "n":
                    confirm = False

        print("\nRolling...")

        half = False
        refund = False
        rarity = genRarity(chance) # Generate Rarity berdasarkan chance yang udah ada
        if rarity != "Failed":

            if rarity in avaRarity:
                iditem, name = getItem(datac, rarity)
                print("\nSelamat, Anda mendapatkan %s (Rank %s)" % (name, rarity))

                # Auto id buat cons_hist
                if len(datah)-1 == 0:
                    idh = "1"
                else:
                    idh = str(int(datah[len(datah)-1][0]) + 1)

                date = datetime.now() # Tanggal diambil tanggal "skrg"
                date = date.strftime("%d/%m/%Y")

                datah.append([idh, userid, iditem, date, 1]) # Item hasil combine jumlahnya fix 1

            else:
                refund = True
                print("\nMaaf, item dengan Rarity %s yang anda dapatkan tidak tersedia di stock" % rarity)
                print("Silahkan minta admin untuk melengkapi rarity consumables")
        
        else: # Failed gacha (safecase)
            print("\nSayang sekali, anda sedang tidak beruntung")
            print("Item yang anda gunakan akan terbuang sebanyak 50%")
            refund = True
            half = True

        for i in range(len(item)):
            idx = item[i][0]
            if half:
                n = item[i][1] // 2
            else:
                n = item[i][1]

            if refund:
                invent[idx][5] = str(int(invent[idx][5]) + n)
                
            if invent[idx][5] == '0':
                invent.pop(idx)
                for j in range(i+1, len(item)):
                    item[j][0] -= 1

    return invent, datac, datah