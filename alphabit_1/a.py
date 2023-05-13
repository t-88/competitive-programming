def func(r, c, curr, res, mat):
    if (curr[0] > r-1 or curr[0] < 0) or (curr[1] < 0 or curr[1] > c):
        return
    elif mat[curr[0]][curr[1]] == 1:
        res.append(curr[0], curr[1])
        func(r,c,[curr[0]--, curr[1]],res, mat)
        func(r,c,[curr[0]++, curr[1]],res, mat)
        func(r,c,[curr[0], curr[1]++],res, mat)
        func(r,c,[curr[0], curr[1]--],res, mat)

        return res
    else:
        return

print(func(5,6,[2,3],[], [[0,0,1,0,1,1], [0,1,0,1,0,1], [0,0,1,1,0,0], [0,1,1,0,0,1], [0,1,0,0,1,0]]))