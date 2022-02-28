class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = {}
        for i in range (len(nums)):
            compliment = target - nums[i]
            if(compliment in s):
                return [s.get(compliment),i]
            s[nums[i]]=i


def main():
    nums = [2,7,11,15]
    target = 9
    object = Solution()
    print(object.twoSum(nums,target))


if __name__ == "__main__":
    main()        