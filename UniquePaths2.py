class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len((obstacleGrid[0])) 
        mem = [[-1]*n for _ in range(m)]
        return self.countPaths(obstacleGrid, m-1,n-1,mem)
    
    def countPaths(self,obstacleGrid, m , n, mem):
        if m<0 or n < 0 or obstacleGrid[m][n] ==1:
            return 0
        if m ==0 ==n:
            return 1
        if mem[m][n] == -1:
            mem[m][n] = self.countPaths(obstacleGrid, m-1,n,mem) + self.countPaths(obstacleGrid, m,n-1,mem)
        return mem[m][n] 
    
def main():
    obstacleGrid = [[0],[0]]
    object = Solution()
    print(object.uniquePathsWithObstacles(obstacleGrid))


if __name__ == "__main__":
    main()  