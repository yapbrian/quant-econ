x_vals = (1,2,3)
y_vals = (9,8,7)

inner_p = 0

# Part 1
#for x,y in zip(x_vals,y_vals):
#    inner_p = inner_p + x*y
inner_p = sum([x*y for x,y in zip(x_vals,y_vals)])
print inner_p

# Part 2
even_nums = sum([x%2 for x in range(100)])
print even_nums

# Part 3
even_pairs = sum([x%2==0 and y%2==0 for x,y in ((2,5),(4,2),(9,8),(12,10))])
print even_pairs