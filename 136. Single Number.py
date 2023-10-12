from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ans = 0
        
        for i in nums:
            ans ^= i
            
        return ans



if __name__ == '__main__':

    lc = Solution()

    nums = [ 4, 1, 2, 1, 2 ]

    print( lc.singleNumber(nums) )
