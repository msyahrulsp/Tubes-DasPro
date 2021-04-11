def Hash(pwd,s=5):
    hasil = ''
    for i in pwd:
        char = i
        if char.isupper(): hasil+=chr((ord(char) + s-65) % 26 + 65)
        else : hasil+=chr((ord(char) + s - 97) % 26 + 97)
    return hasil
