class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        def spiral(matrix,i,j,dir,stepsToTake,stepsTaken):
            ans.append(matrix[i][j])
            if stepsToTake == stepsTaken:
                dir = (dir +1) %4
            if dir == 1:
                spiral(matrix,i,j+1,dir,stepsToTake,stepsTaken+1)
        return ans
        
def main():
    object = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(object.spiralOrder(matrix))

if __name__ == "__main__":
    main()        