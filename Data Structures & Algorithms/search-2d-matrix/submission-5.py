class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top=0
        l = 0
        bottom = ROWS-1
        r = COLS-1

        while top<bottom:
            mid = (top+bottom)//2
            if target >= matrix[mid][l] and target <= matrix[mid][r]:
                top = mid
                break
            if target <= matrix[mid][r] and target < matrix[mid][l]:
                bottom = mid - 1
            elif target > matrix[mid][r]:
                top = mid + 1
        # print(top)
        while l <= r:
            m = (l+r) //2
            # print(l,r,m)
            if target > matrix[top][m]:
                l = m+1
            elif target < matrix[top][m]:
                r = m -1
            else:
                # print(matrix[top][m])
                return matrix[top][m] == target
        return False
    

            
