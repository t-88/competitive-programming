class Solution1:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        a , b  = 0 , len(numbers) - 1
        while True:
            k =  numbers[a] + numbers[b]
            if k == target:
                return [a + 1 , b + 1]
            elif k > target:
                b-=1
            else:
                a+=1
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        a = {}
        for i in range(len(numbers)):
            n1 = numbers[i]             
            n2 = target - n1
            if n2 in a:
                return [a[n2] + 1,i+1]
            a[n1] = i             
print(Solution().twoSum([2,7,11,15],9))                