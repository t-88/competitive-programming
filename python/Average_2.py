#https://www.beecrowd.com.br/judge/en/problems/view/1006
A = float(input())
B = float(input())
C = float(input())

if((A < 0 or A > 10) or (B < 0 or B > 10) or (C < 0 or C > 10)):
    print("Number out of range")
    exit()

print("MEDIA %.1f" % ((A * 2 + B * 3 + C * 5) / (2 + 3 + 5)))