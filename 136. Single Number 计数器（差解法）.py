from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        counter = {}
        
        for i in nums:
            if i not in counter: counter[i] = 1
            else: counter[i] += 1

        for key in counter.keys():
            if counter[key] % 2: return key



if __name__ == '__main__':

    lc = Solution()

    nums = [ 4, 1, 2, 1, 2 ]

    print(lc.singleNumber(nums))
