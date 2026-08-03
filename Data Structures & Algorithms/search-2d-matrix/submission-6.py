class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l<=r:
            mid = (l+r) // 2
            if matrix[mid][-1] < target:
                l = mid +1
            elif matrix[mid][0] > target:
                r = mid -1
            else:  
                n= mid
                r = len(matrix[0]) -1
                l = 0
                while l<=r:
                    mid_n = (l+r) // 2
                    if matrix[n][mid_n] < target:
                        l = mid_n +1
                    elif matrix[n][mid_n] > target:
                        r = mid_n -1
                    else:
                        return True
        return False