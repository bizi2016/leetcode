class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        # 首先，如果数组长度都不够3，直接出局
        if len(arr) < 3: return False

        # 先找到最大点的索引
        max_index = arr.index(max(arr))

        # 如果索引在头尾，直接出局
        if max_index in [0, len(arr)-1]: return False

        # 之后，切分数组（都要包含最大值）
        left, right = arr[:max_index + 1], arr[max_index:]

        # 判断是否有平坦地带
        if len(left) != len(set(left)) or len(right) != len(set(right)):
            return False
        
        # 最后，判断左右是否是坡
        return left == sorted(left) and right == sorted(right, reverse=True)
