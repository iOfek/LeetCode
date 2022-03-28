class Solution(object):
    
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        self.dfs(candidates,target,[],0,ret)
        return ret
    
    
    def dfs(self,candidates,target,path,sum,ret):
        if sum == target :
            ret.append(path)
            return
        if sum > target:
            return
        for i in range(len(candidates)):
            self.dfs(candidates[i:],target,path+[candidates[i]],sum+ candidates[i],ret)
            
            
def main():
    candidates= [3,5,8]
    target = 11
    object = Solution()
    print(object.combinationSum(candidates,target))


if __name__ == "__main__":
    main()  