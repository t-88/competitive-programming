class Solution:
    def check_box(self,bir,bic,game) -> bool:
        # rows
        l = []
        for row in range(3):
            l += game[bir*3 + row][bic * 3:(bic + 1)*3]
        l = list(filter(lambda x: x != "",l))
        return len(set(l)) == len(l)


    def check_col(self,game,index,max_rows = None, start_row = None):
        if max_rows == None:
            max_rows = len(game)
            start_row = 0
        col = []
        for row in range(start_row,len(game)):
            col.append(game[row][index])
        return col
    
    def ValidSudoku(self,game : list[list[str]]) -> bool: 
        # print("rows")
        # rows
        for row in range(len(game)):
            l = list(filter(lambda x: x != "",game[row]))
            if len(l) != len(set(l)):
                return False
        
        # print("cols")
        # cols
        for col in range(len(game[0])):
            whole_col = self.check_col(game,col)
            l = list(filter(lambda x: x != "",whole_col))

            if len(l) != len(set(l)):
                return False                
        
        # print("boxes")
        # box in row: bir
        # box in col: bic
        for bir in range(3):
            for bic in range(3):
                if not self.check_box(bir,bic,game):
                    return False               

        return True

inp = [
       [7, "", 2, 1, 5, 4, 3, 8, 6],
       [6, "", 3, 8, 2, 7, 1, 5, 9],
       [8, "", 1, 3, 9, 6, 7, 2, 4],
       [2, 6, 5, 9, 7, 3, 8, 4, 1],
       [4, 8, 9, 5, 6, 1, 2, 7, 3],
       [3, 1, 7, 4, 8, 2, 9, 6, 5],
       [1, 3, 6, 7, 4, 8, 5, 9, 2],
       [9, 7, 4, 2, 1, 5, 6, 3, 8],
       [5, 2, 8, 6, 3, 9, 4, 1, 7]
       ]



out = Solution().ValidSudoku(inp)
print(out)
