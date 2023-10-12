from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        left, right, up, down = 0, len(matrix[0])-1, 0, len(matrix)-1
        ans = []

        while True:

            for i in range(left, right + 1):
                ans.append(matrix[up][i])
            up += 1
            if up > down: break

            for i in range(up, down + 1):
                ans.append(matrix[i][right])
            right -= 1
            if left > right: break

            for i in range(right, left - 1, -1):
                ans.append(matrix[down][i])
            down -= 1
            if up > down: break

            for i in range(down, up - 1, -1):
                ans.append(matrix[i][left])
            left += 1
            if left > right: break

        return ans



if __name__ == '__main__':

    # matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    
    lc = Solution()
    print(lc.spiralOrder(matrix))
