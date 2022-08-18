def alternate(a1, a2):
    b = []
    c = int(len(a1 + a2))
    i = 0
   
    for i in range(int(len(a1+a2)/2)):
        b.append(a1[i])
        b.append(a2[i])
    return b
