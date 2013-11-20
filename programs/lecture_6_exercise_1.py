def Fibonnaci(t):
    if t <= 0:
        return 0
    if t == 1:
        return 1
    else:
        return Fibonnaci(t-1) + Fibonnaci(t-2)

