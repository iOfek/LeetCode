import re


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret= []
        self.dfs(n,k,[],ret,i=1)
        return ret
    def dfs(self,n,k,path,ret,i):
        if k == 0:
            ret.append(path)
            return
        if k < 0 : 
            return
        for i in range(i,n+1):
            self.dfs(n,k-1,path+[i],ret,i+1)
        
def main():
    n,k = 4,2
    object = Solution()
    print(object.combine(n,k))


if __name__ == "__main__":
    main()  