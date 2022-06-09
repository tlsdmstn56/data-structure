class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start = -1
        max_consecutive_ones = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                start = -1
            else:
                if start < 0:
                    start = i
                max_consecutive_ones = max(max_consecutive_ones, i - start + 1)
        return max_consecutive_ones
