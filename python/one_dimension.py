#https://github.com/AlphaBitClub/alphabit-coding-challenge/blob/master/alphabit-coding-challenge-02/05_one_dimension/one_dimension.pdf


# this challange is wrong 
# they say the count start from 0 
# in the example they give i to be 2 and size of cols = 2, out of range 
# and they give the answer for i = 1 so  they fucked up 



names = input("names: ").split(" ")
size = list(map(int,input("size: ").split(" ")))
index = list(map(int,input("index: ").split(" ")))

index = index[0] + index[1] * size[0]
if index > len(names):
    print("wrong i,j")
else:
    print(names[index])



