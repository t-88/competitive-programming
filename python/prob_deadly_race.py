#https://github.com/AlphaBitClub/alphabit-coding-challenge/blob/master/alphabit-coding-challenge-03/deadly_race/prob-Deadly%20race.pdf

d =  int(input())

number = 2
while d > 3:
    d /= number % 10
    number *= 2


print(number)