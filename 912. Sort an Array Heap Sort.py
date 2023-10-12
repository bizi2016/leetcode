class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        
        # 首先建立最大堆
        # 建立了最大堆改root再heapify会触发连锁反应
        for i in range(n, -1, -1):
            self.heapify(nums, n, i)

        # 把最大值挪到最后已排序列表中（选择排序）
        # 调用heapify进行连锁反应，注意，现在只能用部分数组
        for i in range(n-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, i, 0)

        return nums

    # 向上调整
    def heapify(self, nums, n, i):
        
        left = i*2 + 1
        right = i*2 + 2

        largest = i

        if left < n and nums[left] > nums[largest]:
            largest = left
        if right < n and nums[right] > nums[largest]:
            largest = right

        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.heapify(nums, n, largest)  # 递归，连锁反应
