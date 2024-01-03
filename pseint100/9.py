
XN = 7
for F in range (1,8):
    serie = ""
    if (F >= 5):
        XN = XN + 2
        
    for C in range (XN - F):
        serie = (serie + " * ")
        
    print(serie)