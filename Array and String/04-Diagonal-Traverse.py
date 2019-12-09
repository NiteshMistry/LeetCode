class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        num_rows = len(matrix)
        num_cols = len(matrix[0]) if num_rows > 0 else 0
        if num_cols == 0:
            return []
        
        row,col = 0,0
        a = [0 for i in range(num_rows*num_cols)]
        up = True
        for i in range(num_rows*num_cols):
            a[i] = matrix[row][col]
            if up:
                if col == num_cols-1:
                    row += 1
                    up = not up
                elif row==0:
                    col += 1
                    up = not up
                else:
                    row = row - 1
                    col = col + 1
            else:
                if row == num_rows-1:
                    col += 1
                    up = not up
                elif col == 0:
                    row += 1
                    up = not up
                else:
                    row = row + 1
                    col = col - 1
        return(a)