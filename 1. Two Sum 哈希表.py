class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)

        paired_dict = {}  # 哈希表
        for index in range(n):
            
            # 查找之前的
            if nums[index] in paired_dict:
                return [ index, paired_dict[ nums[index] ] ]

            # 加入本次的
            paired_dict[ target - nums[index] ] = index

        return []
