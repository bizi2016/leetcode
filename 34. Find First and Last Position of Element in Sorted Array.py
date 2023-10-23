class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        result = [-1, -1]
        n = len(nums)
        if n == 0: return result

        left, right = 0, n-1

        while left < right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        
        if nums[left] != target:
            return result
        
        result[0] = left



        left, right = 0, n-1

        while left < right:
            mid = (left + right + 1) // 2
            if target >= nums[mid]:
                left = mid
            else:
                right = mid - 1
        
        result[1] = right
        
        return result
