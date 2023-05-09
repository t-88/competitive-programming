#https://github.com/AlphaBitClub/alphabit-coding-challenge/blob/master/alphabit-coding-challenge-02/04_the_keypad/the_keypad.pdf
inputs = [[" "],["A", "B", "C"],["D", "E", "F"],["G", "H", "I"],["J", "K", "L"],["M", "N", "O"],["P", "Q", "R", "S"],["T", "U", "V"],["W", "X", "Y", "Z"]]



seq = input("seq: ").split(" ")

for i in range(len(seq)):
    key = int(seq[i][0]) - 1
    if key == -1: key = 0
    
    offset = (len(seq[i]) - 1) % (len(inputs[key]))

    print(inputs[key][offset],end='')

print()