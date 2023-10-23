class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums = self.qs(nums)
        return nums[ len(nums)-k ]

    def qs(self, nums):

        if len(nums) <= 1:
            return nums

        pivot = random.choice(nums)
        left, mid, right = [], [], []

        for i in nums:
            if i < pivot: left.append(i)
            elif i > pivot: right.append(i)
            else: mid.append(i)
        
        return self.qs(left) + mid + self.qs(right)
