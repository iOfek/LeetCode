import string


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        """
        pick 2 indexes starting from the middle 
        
        """
        l =0
        r =0
        first = True
        max_length = 1
        index = 0
        for i in range(len(s)):
            l=i-1
            r=i+1
            counter =1;
            while True:
                if (l<0 or r>len(s)-1) or (s[l] != s[r]):
                    break    
                counter+=2
                l-=1
                r+=1
            if max_length < counter :
                max_length = counter
                index = i
        
        
        for i in range(len(s)):
            l=i-1
            r=i
            counter =0
            while True:
                if (l<0 or r>len(s)-1) or (s[l] != s[r]):
                    break    
                counter+=2
                l-=1
                r+=1
            if max_length < counter :
                max_length = counter
                index = i
                first = False
        
        
        if first:
            startIndex= index-int((max_length-1)/2)
            endIndex= startIndex + max_length
        else:
            startIndex= index-int((max_length)/2)
            endIndex= startIndex + max_length
        
        
        
        
        
        
        return s[startIndex:endIndex]
        
 
        
        
def main():
    object = Solution()
    print(object.longestPalindrome("babad"))
    print(object.longestPalindrome("cbbd"))


if __name__ == "__main__":
    main()