
def p(x, coeff):
    #sum = 0
    #for index, a_coeff in enumerate(coeff):
    #    sum = sum + a_coeff * x**index
    #return sum
    return sum(a*x**i for i,a in enumerate(coeff))
    
