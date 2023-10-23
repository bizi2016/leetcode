class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]: left = mid + 1
            elif target < nums[mid]: right = mid - 1
            else: return mid
        
        return left



class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        # 定义target在左闭右开的区间里
        left, right = 0, n 

        while left < right:
            mid = (left + right) // 2
            if target > nums[mid]: left = mid + 1
            elif target < nums[mid]: right = mid
            else: return mid
        
        return right
