M = int(input())
N = list(map(int,input().split(' ')))
m = list(map(int,input().split(' ')))


def occ(arr):
    
    a = []
    b = {} 
    for i in arr:
        if not (i in a):
            a.append(i)
            b[str(i)+"_"] = arr.count(i)
    return b



def function(M,N,m):
    used =  occ(m)
    storage = []
    sum = 0
    for i in m:
        if not(i in storage):
            val = N[i]
            if val <= M:
                if val + sum > M:
                    while val + sum > M:
                        b = {}
                        for d in storage:
                            b[str(d)+"_"] = used[str(d)+"_"]
                        a = [b[val] for val in b]
                        r = [val for val in b]
    
                        index_min =  a.index(min(a))
                        r = int(r[index_min][:1])

                        sum -= N[r]
                        if len(storage) == 1:
                            storage = []
                        else:
                            storage.remove(storage.index(r))

                    storage.append(i)
                    sum += val

                else:
                    storage.append(i)
                    sum += val
    return sum 

print(function(M,N,m))
