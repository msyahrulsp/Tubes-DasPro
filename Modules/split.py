def split(txt,case=','):
    s=[]
    j=0
    for i in range (len(txt)):
        if case== txt [i]:
            s.append(txt[j:i])
            j=i+1
    s.append (txt[j:])
    return [ item for item in s if item ]