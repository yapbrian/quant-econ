
def capCount(inputstring):
    return sum(char1==char2 for char1,char2 in zip(inputstring, inputstring.upper()))    
