import sys


tests_count = int(sys.stdin.readline())

lines = []
for _ in range(tests_count):
    lines.append(sys.stdin.readline().strip())


def solve(n,k,x):
    k = list(range(1,min(k+1,n+1)))
    k.pop(x-1)

    if len(k) == 0:
       print("NO") 
       return
    curr = n
    taken = []
    while len(k) > 0 and n != 0:
        curr -= k[0]
        if curr >= 0:
            n = curr
            taken.append(str(k[0]))
        else:
            curr = n + int(taken[-1])
            taken.pop()
            k.pop(0)

    if n == 0:
        print("YES")
        print(len(taken))
        print(" ".join(taken))
    else:
        print("NO")

    
for line in lines:
    a = list(map(int,line.split(" ")))
    solve(a[0],a[1],a[2])



