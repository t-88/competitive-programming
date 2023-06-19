from collections import defaultdict

from collections import defaultdict

class TimeMap(object):

    def __init__(self):
        self.table = defaultdict(list)

    def set(self, key, value, timestamp):
        self.table[key].append([timestamp, value])

    def get(self, key, timestamp):
        if key not in self.table:
            return ""
        
        l , r = 0 , len(self.table[key]) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if self.table[key][mid][0] == timestamp:
                return self.table[key][mid][1]
            elif self.table[key][mid][0] <= timestamp:
                res = self.table[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res

table = TimeMap();  
tests = [["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
for test in tests:
    if len(test) == 3:
        print(table.set(test[0],test[1],test[2]))
    else:
        print(table.get(test[0],test[1]))

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)