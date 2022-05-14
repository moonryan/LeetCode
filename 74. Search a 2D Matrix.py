from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up, down = 0, len(matrix) - 1
        while up <= down:
            n = (up + down) // 2

            if target < matrix[n][0]:
                down = n - 1
            elif target > matrix[n][-1]:
                up = n + 1
            else:
                break
        
        if not up <= down:
            return False

        else:
            l, r = 0, len(matrix[n]) - 1
            while l <= r:
                m = (l + r) // 2

                if matrix[n][m] > target:
                    r = m - 1
                elif matrix[n][m] < target:
                    l = m + 1
                else:
                    return True

            return False
