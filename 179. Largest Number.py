from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        import functools

        def cmp(a, b):
            if a+b == b+a: return 0
            elif a+b > b+a: return 1
            else: return -1

        nums_str= list(map(str, nums))
        nums_str.sort(key = functools.cmp_to_key(cmp), reverse=True)

        return str(int(''.join(nums_str)))



if __name__ == '__main__':

    nums = [ 3, 30, 34, 5, 9 ]
    # nums = [ 0, 0, 0, 0 ]

    lc = Solution()
    print( lc.largestNumber(nums) )
