#https://github.com/AlphaBitClub/alphabit-coding-challenge/blob/master/alphabit-coding-challenge-01/02_memory_size/memory_size.pdf
import math
import random


x = 1000
d = []
for i in range(x):
    k = random.randint(1,10)
    d.append(k)


a = sum(d)
m = math.ceil(math.log(a,2))
print(1<<m)

