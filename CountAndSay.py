class Solution(object):
      
    
    
    
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def say(number):
            string = ""
            count = 1
            nextDigit = number[0]
            for i in range(1,len(number)):
                if number[i] == nextDigit:
                    count+=1
                # different number 
                else:
                    string = string + str(count) + nextDigit
                    nextDigit = number[i]
                    count=1
            
            string += str(count) +nextDigit   
            return string 
         
        def count(n):   
            str = "1"
            # n > 1
            while(n>1):
                str= say(str)
                n-=1
            
            return str
        return count(n)    
        

def main():
    object = Solution()
    n = 4
    print (object.countAndSay(n))


if __name__ == "__main__":
    main() 