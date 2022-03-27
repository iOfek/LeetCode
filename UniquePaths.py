
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def path(m,n):
            if m==0 and n == 0:  
                return 1
            if m < 0 or n < 0 :
                return 0
            if  mem[m][n] == -1:
                mem[m][n] = path(m-1,n) + path(m,n-1) 
            return mem[m][n]
                
        mem = [[-1] * n for _ in range(m)]
        return path(m-1,n-1)
        
def main():
    object = Solution()
    m= 7
    n= 3
    print (object.uniquePaths(m,n))


if __name__ == "__main__":
    main() 