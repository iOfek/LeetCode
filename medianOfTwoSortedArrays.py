class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # even
        if len(nums1 +nums2 ) % 2 == 0:
            index1,index2 = len(nums1 +nums2)/2 , len(nums1 +nums2)/2 -1
        else:
            index = int(len(nums1 +nums2)/2 )
def main():
    nums1 = [1,3]
    nums2 = [2]
    nums3 = [1,2]
    nums4 = [3,4]
    object = Solution()
    print(object.findMedianSortedArrays(nums1,nums2))
    print(object.findMedianSortedArrays(nums3,nums4))


if __name__ == "__main__":
    main()