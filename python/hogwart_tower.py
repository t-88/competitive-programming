#https://github.com/AlphaBitClub/alphabit-coding-challenge/blob/master/alphabit-coding-challenge-02/06_hogwarts_towers/hogwarts_towers.pdf

lens = list(map(int,input().split(" ")))
lens_set = set(lens)
if len(lens_set) != len(lens):
    print("fall")
else: 
    indexs = [[i,lens[i - 1]] for i in range(1,len(lens) + 1)]
    indexs = sorted(indexs, key=lambda x:x[1],reverse=True)
    indexs = [indexs[i][0] for i in range(len(lens))]
    print(indexs)