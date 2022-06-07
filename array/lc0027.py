class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        removed = 0
        i = 0
        while i < len(nums) - removed:
            if nums[i] != val:
                i += 1
                continue
            for j in range(i+1, len(nums) - removed):
                nums[j-1] = nums[j] 
            removed += 1
        return len(nums) - removed
