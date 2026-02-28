import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

while True:
    try:
        C, H, O = input().split()
        C = int(C) // 2
        H = int(H) // 6
        O = int(O)
        print(min(C, H, O))
    except EOFError:
        break