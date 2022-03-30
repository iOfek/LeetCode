from numpy import sort


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = []
        sorted(strs[0])
        while(strs):
            path = [strs.pop()]
            sorted_characters_first = sorted(path[0])
            sorted_first = "".join(sorted_characters_first)
            indexes=[]
            for i in range(0,len(strs)):
                sorted_characters = sorted(strs[i])
                sorted_str = "".join(sorted_characters)
                if  sorted_str== sorted_first:
                    indexes.append(strs[i])
                    path.append(strs[i])
            ret.append(path)
            for index in indexes:
                strs.remove(index)
        return ret
    
    def group(self,strs,path,ret):
        for i in range ( len( strs)):
            self.group(strs,path,ret)
        return
        
def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    object = Solution()
    print(object.groupAnagrams(strs))


if __name__ == "__main__":
    main()  