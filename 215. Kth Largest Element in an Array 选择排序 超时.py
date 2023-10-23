class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        n = len(nums)

        for i in range(k):
            max_index = i
            for j in range(i, n):
                if nums[j] > nums[max_index]:
                    max_index = j
            if max_index != i:
                nums[i], nums[max_index] = nums[max_index], nums[i]
        
        return nums[i]
