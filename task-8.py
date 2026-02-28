import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

while True:
    try:
        line = input()
        print(f"{line}!!!")
    except EOFError:
        break