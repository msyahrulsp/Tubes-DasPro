from Util.split import split

def delItem(data, id, type):
    if type == "gadget":
        item = data[0] # Gadget
        deleted = data[1] # Deleted
    else:
        item = data # Consumables

    for i in range(len(item)):
        datasplit=item[i]
        if datasplit[0] == id:
            opsi = input(f"Apakah anda yakin ingin menghapus {datasplit[1]} (Y/N)? ").lower()
            if opsi == 'y':
                print("\nItem telah berhasil dihapus dari database")
                if type == "gadget":
                    item[i][3] = "0" # Deleled item langsung punya 0 item
                    deleted.append(item[i])
                    item.pop(i)
                    return item, deleted
                item.pop(i)
                return item
            elif opsi != "n":
                print("\nInput invalid")
             
            if type == "gadget":
                return item, deleted
            return item

    print(f"\nTidak ada item dengan id: {id}")

    if type == "gadget":
        return item, deleted
    return item



