
def linapprox(func, a, b, n, x):
    space_sz = (b - a)/(n-1)
    f_at_x = 0
    for i in range(n):
        print a+space_sz*i
        if a+space_sz*i <= x and x <= a+space_sz*(i+1):
            # interpolate
            u, v = a+space_sz*i, a+space_sz*(i+1)
            f_at_x = ((func(v)-func(u))/space_sz)*(x-u)+func(u)
    return f_at_x
