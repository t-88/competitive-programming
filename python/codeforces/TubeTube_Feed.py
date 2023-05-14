#https://codeforces.com/contest/1822/problem/A
#12:47PM -> 1:12PM

tests = int(input())

for i in range(tests):
    time = list(map(int,input().split(" ")))[1]
    dur = list(map(int,input().split(" ")))
    ent = list(map(int,input().split(" ")))

    def sol(ent,dur,time):
        combine = [[dur[i] + i,ent[i],i] for i in range(len(ent))]
        combine = list(filter(lambda x: x[0] <= time,combine))
        if len(combine) == 0: return "-1"
        return max(combine,key=lambda x : x[1])[2] + 1
        





    print(sol(ent,dur,time))