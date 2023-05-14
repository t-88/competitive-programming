#https://codeforces.com/contest/1822/problem/B
#1:16PM -> 1:44

tests = int(input())

for i in range(tests):
    input()
    arr = list(map(int,input().split(" ")))

    def getB(arr):
        if len(arr) <= 1:
            return 0
        arr = [arr[i] * arr[i + 1] for i in range(len(arr) - 1)]
        return max(arr)
    def sol(arr):
        if len(arr) == 2:
            return arr[0] * arr[1]
        arr = sorted(arr)
        nigs = list(filter(lambda x : x <= 0, arr))
        poss = list(filter(lambda x : x > 0, arr))

        poss = poss[-2:]
        nigs = nigs[:2]

        return max(getB(poss),getB(nigs))

    print(sol(arr))