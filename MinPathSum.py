class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid), len(grid[0])
        mem = [[0]*n for _ in range(m)]
        mem[0][0]= grid[0][0]
        return self.path(grid,m-1,n-1,mem)
    
    
    def path(self,grid,m,n,mem):
        if m==0==n:
            return grid[m][n]
        if m<0 or n<0:
            return float('inf')
        if mem[m][n] == 0:
            mem[m][n] =grid[m][n] + min(self.path(grid,m-1,n,mem) , self.path(grid,m,n-1,mem))
        return mem[m][n]
        
def main():
    grid = [[1,2,5],[3,2,1]]
    object = Solution()
    print(object.minPathSum(grid))


if __name__ == "__main__":
    main()  