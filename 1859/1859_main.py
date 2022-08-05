import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    num_prices = int(input())
    prices = list(map(int, input().split(' ')))

    profit = 0
    cur_price = 0
    for x in range(num_prices):
        selling_price = prices[-1 - x]
        if selling_price > cur_price:
            cur_price = selling_price
        else:
            profit = profit + (cur_price - selling_price)

    print(f"#{test_case} {profit}")
