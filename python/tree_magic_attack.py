#https://github.com/AlphaBitClub/alphabit-coding-challenge/blob/master/alphabit-coding-challenge-02/08_tree_magic/tree_magic.pdf

gen = int(input("gen: "))
a = sum([i * 2**(i - 1) for i in range(gen + 1)])
print(a)