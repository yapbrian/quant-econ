from random import uniform

def silly_game(n):
    head_count = 0
    cash_count = 0
    for i in range(n):
        coinflip = uniform(0, 1)
        head_count = head_count + 1 if coinflip < 0.5 else 0
        if head_count == 3:
            cash_count = 1
    return cash_count

cash = silly_game(10)
print cash
