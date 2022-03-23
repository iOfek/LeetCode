class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        
        
        
        n = len(matrix)
        for row in range((n//2) +n % 2):
            for col in range((n//2)):
                temp = matrix[row][col]
                matrix[row][col] = matrix[n-1-col][row]
                matrix[n-1-col][row]= matrix[n-1-row][n-1-col]
                matrix[n-1-row][n-1-col] = matrix[col][n-1-row]
                matrix[col][n-1-row] = temp
                
            
        
def main():
    object = Solution()
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    print (object.rotate(matrix))
    print(matrix)


if __name__ == "__main__":
    main() 