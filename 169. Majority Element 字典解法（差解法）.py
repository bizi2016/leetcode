class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # 统计
        counter = {}
        for i in nums:
            if i in counter: counter[i] += 1
            else: counter[i] = 1
        
        # 找最多
        max_c = [0, 0]
        for v, c in counter.items():
            if c > max_c[1]:
                max_c = [v, c]

        return max_c[0]
