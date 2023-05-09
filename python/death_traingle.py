#https://github.com/AlphaBitClub/alphabit-coding-challenge/blob/master/alphabit-coding-challenge-03/death_triangle/prob-Death%20Triangle.pdf
import math


a = list(map(int,input().split(" ")))
b = list(map(int,input().split(" ")))
c = list(map(int,input().split(" ")))

ab = [a[0]-b[0],a[1]-b[1]]
bc = [c[0]-b[0],c[1]-b[1]]
ac = [a[0]-c[0],a[1]-c[1]]

ac = math.sqrt(ac[0] * ac[0] + ac[1] * ac[1])
ab = math.sqrt(ab[0] * ab[0] + ab[1] * ab[1])
bc = math.sqrt(bc[0] * bc[0] + bc[1] * bc[1])


print(True in [  
               ac * ac ==  ab * ab + bc * bc ,
               ab * ab == ac * ac + bc * bc,
               bc * bc == ac * ac + ab * ab
              ])