#https://leetcode.com/problems/next-greater-element-iii/


class Solution(object):
    def nextGreaterElement(self, n):
        splited = [i for i in str(n)]

        c = -2
        u = []
        a = []
        while (u == a) and c != -(len(splited)):
            u = splited[c:]
            a = sorted(u,reverse=True)
            c -= 1
            print(a, u)
        print(a)            
        
        splited = [val for i , val in enumerate(splited) if i < len(splited) + c]
        splited.extend(a)
        r = int("".join(splited))


        return r 

n = int(input())
a = Solution()
print(a.nextGreaterElement(n))


