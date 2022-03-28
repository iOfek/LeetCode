
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        self.dfs(sorted(candidates),target,0,[],ret)
        return ret
    
    def dfs(self,candidates,target,sum,path,ret):
        if sum == target:
            ret.append(path)
            return
        if sum > target:
            return
        for i in range(len(candidates)):
            if i >0 and candidates[i] == candidates[i-1]:
                continue
            self.dfs(candidates[i+1:],target,sum+ candidates[i],path+[candidates[i]],ret)

def main():
    candidates = [10,1,2,7,6,1,5]
    target = 8
    object = Solution()
    print(object.combinationSum2(candidates,target))


if __name__ == "__main__":
    main()          
        