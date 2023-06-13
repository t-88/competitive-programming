# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for idx , char in  enumerate(s):
            sub = [char]    
            for idx in range(idx + 1,len(s)):
                if s[idx] in sub:    
                    break
                else:
                    sub.append(s[idx])
            if longest < len(sub):
                longest = len(sub)  
            if longest == len(s):
                return longest
        return longest
# sliding window  
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        out = []
        biggest = 0
        for idx  in  range(0,len(s)):
            out.append(s[idx])
            while len(set(out)) != len(out): 
                out.pop(0)
            if len(out) > biggest:
                biggest = len(out)
        return biggest  
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        out = {}
        l = 0
        biggest = 0
        for r  in  range(len(s)):
            if s[r] in out and out[s[r]] >= l:
                l = out[s[r]] + 1
            else:
                biggest = max(biggest,r - l + 1)
            out[s[r]] = r
        return biggest
print(Solution().lengthOfLongestSubstring("tmmzuxt"))
