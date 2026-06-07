class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        top = 0
        r = len(matrix[0]) -1
        bottom = len(matrix) -1

        while top<bottom:
            mid = (top + bottom) // 2
            # print(mid)
            if target >= matrix[mid][l] and target <= matrix[mid][r]:
                top = mid
                # print("here")
            if target > matrix[mid][r]:
                top = mid + 1
            else:
                bottom = mid - 1
        # print(top) 
        while l <= r:
            m = (l+r) //2
            # print(m, matrix[top][m])
            if target == matrix[top][m]:
                return True
            if target >= matrix[top][m]:
                l = m + 1
            else:
                r = m - 1
        return False