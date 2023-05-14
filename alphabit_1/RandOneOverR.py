# valid
# parse 
import math
index = 0

from ast import literal_eval

toTuple = literal_eval("(10, [20, 30]) ")
toTuple = literal_eval("((5, [10, 2]), ([20, 30], 10, [20, 40])) ")
toTuple = literal_eval("(10, 5, 16, [(16, 14), [(15, 10), 5]]) ")
toTuple = literal_eval("(5, 8, 9, [10, 24])")

sum = 0


class Sol():
    def __init__(self) -> None:
        pass


    def serie(self,x):
        sum = 0
        for i in x:
            if type(i) == int:
                sum += i
            elif type(i) == list:
                sum += self.para(i) 
            elif type(i) == tuple:
                sum += self.serie(i)
        return sum

    def para(self,x):
        sum = 0
        for i in x:
            if type(i) == int:
                sum += 1 / i
            elif type(i) == list:
                sum += 1/ self.para(i) 
            elif type(i) == tuple:
                sum += 1 / self.serie(i)
        return 1 / sum

sol = Sol()

if type(toTuple) != tuple:
    toTuple = (toTuple,)
print(toTuple)

print(round(sol.serie(toTuple),2))
