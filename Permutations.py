
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        n = len(nums)
        def rec( nums,group ):
                if len(group) == n:
                    ans.append(group)
                    return
            
                for i in range(len(nums)):
                    num = nums.pop(i)
                    newGroup = list(group)
                    newGroup.append(num)
                    rec(nums, newGroup )
                    nums.insert(i,num)
                    newGroup = list(group)
                    
            

                
        group = []
        rec(nums, group)
        return ans

def main():
    object = Solution()
    nums = [1,2]
    print (object.permute(nums))


if __name__ == "__main__":
    main() 