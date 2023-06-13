class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }
        for char in s:
            if char in ['(','[','{']:
                stack.append(char)
            else:
                if len(stack) == 0 or stack[len(stack)-1] != dic[char] : return False
                stack.pop()
        return len(stack) == 0

print(Solution().isValid("([])"))