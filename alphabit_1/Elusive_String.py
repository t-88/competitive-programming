S = input()
nm = list(map(int,input().split(' ')))
pairs = []
for i in range(nm[0]):
    a = input()
    a = [char for char in a]
    pairs.append(a)


def func(s, nm, mat):
    l = len(s)

    for i in range(1, nm[0]+1):
        
        for j in range(1, nm[1]+1):
            temp = ''
            idx = j
            for char in range(l):
                temp += mat[i-1][(idx-1) % nm[1]]
                idx += 1
            if temp == s:
                return f"row: {i}"
    
    for j in range(1, nm[1]+1):
        
        for i in range(1, nm[0]+1):
            temp = ''
            idx = i
            for _ in range(l):
                temp += mat[(idx-1) % nm[0]][j-1]
                idx += 1
            if temp == s:
                return f"col: {j}"
    
    return 'none'

print(func(S,nm, pairs))