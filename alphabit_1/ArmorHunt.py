# nm = list(map(int,input().split(' ')))
# prices = list(map(int,input().split(' ')))
# pairs = []
# for i in range(nm[1]):
#     pairs.append(sorted(list(map(int,input().split(' ')))))





def function(n, m, prices,pairs):
    if m < 3:
        return "-1"
    
    aa = set()  
    for pair1 in pairs:
        for pair2 in pairs:
            if pair1 != pair2 and  (pair1[0] in pair2 or pair1[1] in pair2):
                p = pair1 + pair2
                p = list(dict.fromkeys(p))
                print(p)
                print('=>',prices[p[0] - 1] + prices[p[1] - 1] + prices[p[2] - 1],"->",p[0] - 1 , p[1] - 1 , p[2] - 1)
                aa.add(prices[p[0] - 1] + prices[p[1] - 1] + prices[p[2] - 1])
    
    if len(aa) == 0:    
        return "-1"
    print(aa)
    return str(min(aa))
print(function(5 , 3,[3,8,7,3,9],[[4,5],[2,5],[1,4]]))
