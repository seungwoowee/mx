import sys

sys.stdin = open("sample_input.txt", "r")


def possible_check(cards):
    if len(cards) % 2 == 0:
        return "no"
    else:
        return "yes"


T = int(input())

for test_case in range(1, T + 1):
    cards = list(map(int, input()))
    print("#%d %s" % (test_case, possible_check(cards)))
