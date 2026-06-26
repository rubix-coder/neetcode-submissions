class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        best = 0
        for n in numSet:
            if n - 1 not in numSet:          # only start a sequence at its head
                length = 1
                while n + length in numSet:
                    length += 1
                best = max(best, length)
        return best