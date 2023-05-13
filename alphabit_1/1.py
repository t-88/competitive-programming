p = int(input())
nP = list(map(int,input().split(' ')))
iP = list(map(int,input().split(' ')))

def function(p, nP, iP):
    for n in range(0,len(iP),2):
        if n > 0 and n < len(iP):
            if nP[iP[n]] + 1 > p:
                return "false"
            
    if(n > 0 and n < len(iP)):
        return "false"
    return "true"    

print(function(p,nP,iP))
