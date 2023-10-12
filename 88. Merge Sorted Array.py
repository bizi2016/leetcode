'''
# 测试
for i in range(0):
    print(i, end=' ')
'''

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        index1 = m - 1
        index2 = n - 1

        index = m + n - 1

        for i in range(index + 1): # len

            if index1 + 1 == 0: # len1 == 0
                for j in range(index2 + 1): # len2
                    nums1[index] = nums2[index2]
                    index -= 1; index2 -= 1
                break

            if index2 + 1 == 0: # len2 == 0
                for j in range(index1 + 1): # len1
                    nums1[index] = nums1[index1]
                    index -= 1; index1 -= 1
                break


            if nums1[index1] > nums2[index2]:
                nums1[index] = nums1[index1]
                index -= 1; index1 -= 1
            else:
                nums1[index] = nums2[index2]
                index -= 1; index2 -= 1
        """
        index1 = m - 1
        index2 = n - 1

        index = m + n - 1

        while index1 >= 0 and index2 >= 0:
            if nums1[index1] > nums2[index2]:
                nums1[index] = nums1[index1]
                index1 -= 1
            else:
                nums1[index] = nums2[index2]
                index2 -= 1
            index -= 1
        
        nums1[:index2 + 1] = nums2[:index2 + 1]



if __name__ == '__main__':

    lc = Solution()

    nums1 = [ 1, 2, 3, 0, 0, 0 ]; m = 3
    nums2 = [ 2, 5, 6 ]; n = 3

    lc.merge(nums1, m, nums2, n)

    print(nums1)
    
