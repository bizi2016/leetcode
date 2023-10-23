# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # 递归边界条件（千万不要忘了）
        if root == None: return None

        # 先拆分到最底层（归并排序第一步）
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # 从底层交换左右
        root.left = right
        root.right = left

        return root
