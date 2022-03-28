class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        
        
        def dfs(nums, path):
            ans.append(path)
            for i in range(len(nums)):
                if i>0 and nums[i]== nums[i-1]:
                    continue
                dfs(nums[i+1:],path+[nums[i]])
        dfs(nums,[])
        return ans
        
def main():
    nums = [1,2,2]
    object = Solution()
    print(object.subsetsWithDup(nums))


if __name__ == "__main__":
    main()  