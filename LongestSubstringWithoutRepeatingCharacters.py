from numpy import character


class Solution(object):
    
    
    def lengthOfLongestSubstring(self, s) -> int:
        """
        :type s: str
        :rtype: int
        """
        used_characters =[]
        counter=0
        max_length = 0
        for startIndex in range(len(s)):
            used_characters =[]
            counter=0
            substring = s[startIndex:]
            for char in substring:
                if char not in used_characters:
                    used_characters.append(char)
                    counter+=1
                else:
                    break
            max_length = max(max_length,counter)
                    
                
        

        return max_length    

def main():
    object = Solution()
    print(object.lengthOfLongestSubstring("pwwkew"))
    print(object.lengthOfLongestSubstring("aab"))
    print(object.lengthOfLongestSubstring("dvdf"))
    



if __name__ == "__main__":
    main()