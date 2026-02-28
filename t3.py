import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

while True:
    try:
        W, H, R = input().split()
        W = int(W)
        H = int(H)
        R = int(R)
        if H  > R * 2 and W > R * 2:
            print("YES")
        else :
            print("NO")
    except EOFError:
        break