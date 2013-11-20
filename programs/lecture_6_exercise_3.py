
f = open('numbers.txt', 'r')

total = 0.0
for line in f:
    try:
        total += float(line)
    except ValueError:
        pass

f.close
print total
