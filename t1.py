import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

while True:
    try:
        month = int(input())
        if month > 12 or month == 0:
            print("Error") 

        if month == 12 or month == 1 or month == 2:
            print("Winter")

        if month == 3 or month == 4 or month == 5:
            print("Spring")

        if month == 6 or month == 7 or month == 8:
            print("Summer")

        if month == 9 or month == 10 or month == 11:
            print("Autumn")

    except EOFError:
        break