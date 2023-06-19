t = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"A":4,"B":9,"C":40,"D":90,"E":400,"F":900}


class Solution1:
    def romanToInt(self, s: str) -> int:
        output = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i]+s[i+1] in t:
                output += t[s[i]+s[i+1]]
                i+=1
            else:
                output += t[s[i]]
            i+=1
        return output

class Solution:
    def romanToInt(self, s: str) -> int:
        while "IV" in s:
            s= s.replace("IV","A")
        while "IX" in s:
            s= s.replace("IX","B")

        while "XL" in s:
            s= s.replace("XL","C")
        while "XC" in s:
            s= s.replace("XC","D")
        while "CD" in s:
            s= s.replace("CD","E")
        while "CM" in s:
            s= s.replace("CM","F")


        output = 0
        for char in s:
            output += t[char]
        return output    
    
print(Solution().romanToInt("IV"))