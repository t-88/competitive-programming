class Solution:
    def isAnagram(self, a,b) -> bool:
        return sorted(list(a)) == sorted(list(b))