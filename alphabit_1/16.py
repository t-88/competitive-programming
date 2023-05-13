a = int(input())
b = int(input())

c = 0
for x in range(0,a,b):
    for y in range(0,a,b):
        if x*x + y*y < a * a:
            c += 1

print(c)