def split(line,delim=','):
    s=[]
    j=0
    for i in range (len(line)):
        if delim== line [i]:
            s.append(line[j:i])
            j=i+1
    s.append (line[j:])
    return [ item for item in s if item ]