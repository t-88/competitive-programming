from  collections import defaultdict
class Solution1:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:    
        tb = defaultdict(list)
        for str in strs:
            tb["".join(sorted(list(str)))].append(str)

        return list(tb.values())


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:    
        tb = {}
        for str in strs:
            sted = "".join(sorted(list(str)))
            if sted in tb:
                tb[sted].append(str)
            else:
                tb[sted] = [str]

        return list(tb.values())
    
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))