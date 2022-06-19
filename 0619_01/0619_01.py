import sys

sys.stdin = open("input.txt", "r")

list = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
sum = 0
while list:
    k = list.pop()
    if k >= 80:
        sum += k

print('%d' % sum)


