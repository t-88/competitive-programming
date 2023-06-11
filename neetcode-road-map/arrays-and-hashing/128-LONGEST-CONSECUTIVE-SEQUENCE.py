class Solution:
    def longest(self, nums: list[int]) -> list[int]:
        longest_seq = []
        for num in nums:
            if num - 1 not in nums:
                seq = [num]
                while(num + 1 in nums):
                    seq.append(num+1)
                    num = num + 1
            if len(seq) > len(longest_seq):
                longest_seq = list(seq)

        return longest_seq


print(Solution().longest([1,100,2,3,200,4]))
