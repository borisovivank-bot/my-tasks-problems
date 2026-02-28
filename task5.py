a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a > b and a > c:
    if a > 94 and a < 727:
        print(a)
    else:
        print ("Error") 

if c > b and c > a:
    if c > 94 and c < 727:
        print(c)
    else:print ("Error")

if b > c and b > a:
    if b > 94 and b < 727:
        print(b)
    else:
        print ("Error") 


