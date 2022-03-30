class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ret = []
        self.dfs(k,n,[],0,ret,1)
        return ret
    def dfs(self,k , n, path , sum, ret,start_index ):
        if k == 0 and sum == n:
            ret.append(path)
            return
        if k < 0 or (k == 0 and sum != n) or sum > n:
            return
        for i in range(start_index,min(n,10)):
            self.dfs(k-1,n,path+[i],sum+i,ret,i+1)
        
def main():
    k, n  = 9 , 45
    object = Solution()
    print(object.combinationSum3(k, n))


if __name__ == "__main__":
    main()  