class Solution1:
    def longestCommonPrefix2(self, strs: list[str]) -> str:
        k = 0
        b = min(len(strs[0]),len(strs[1])) 
        while(k < b and strs[0][k] ==strs[1][k] ):
            k += 1
        if k == b - 1 and strs[0][k] == strs[1][k]:
            k += 1
        return strs[0][:k]
            
    def longestCommonPrefix(self, strs: list[str]) -> str:
        a = strs[0]
        for str in range(1,len(strs)):
            a = self.longestCommonPrefix2([a,strs[str]])
            if a == "": return ""
        return a
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ma = max(strs)
        mi = min(strs)
        b = min(len(ma),len(mi)) 

        output = ""
        for i in range(b):
            if ma[i] == mi[i]:
                output += mi[i]
            else:
                break
        return output
            
            

print(Solution().longestCommonPrefix(["flower","flow","flight"]))