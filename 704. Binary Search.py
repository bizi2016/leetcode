from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        left, right = 0, n-1

        while left <= right:
            
            mid = (left + right) // 2
            
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        
        return -1



if __name__ == '__main__':
    
    nums = [-1,0,3,5,9,12]
    target = 9
    '''
    nums = [-1,0,3,5,9,12]
    target = 2
    '''
    lc = Solution()
    print(lc.search(nums, target))
