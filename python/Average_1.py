#beecrowd.com.br/judge/en/problems/view/1005
A = float(input())
B = float(input())

if(A < 0 or A > 10):
    print("A out of range")
    exit()
if(B < 0 or B > 10):
    print("B out of range")
    exit()    

print("MEDIA %.5f" % ((A * 3.5 + B * 7.5) / 11))