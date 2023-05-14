#https://codeforces.com/contest/1822/problem/C
#12:30AM -> 12:50AM

def calc(n):
    return n**2 + 2*n - 24  + 26


tests = int(input())

for i in range(tests):
    n = int(input())

    print(calc(n))
