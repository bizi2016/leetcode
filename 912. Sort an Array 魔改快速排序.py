import random
from typing import List



class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        # Recursive boundary conditions
        if n == 0 or n == 1:
            return nums

        # Quick sort python
        pivot = random.choice(nums)
        left, mid, right = [], [], []

        for i in nums:
            if i < pivot: left.append(i)
            elif i > pivot: right.append(i)
            else: mid.append(i)
        
        return self.sortArray(left) + mid + self.sortArray(right)



if __name__ == '__main__':

    lc = Solution()

    nums, ans = list(range(20)), list(range(20))

    for i in range(100000):
        
        random.shuffle(nums)
        nums = lc.sortArray(nums)
        
        if nums != ans:
            print(nums)
















