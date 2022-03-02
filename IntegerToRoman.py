class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        map = {}
        map [1] = "I"
        map [5] = "V"    
        map [10] = "X"    
        map [50] = "L"    
        map [100] = "C" 
        map [500] = "D"        
        map [1000] = "M" 
        
        # problem digits, 1,4,6,9
        ones = num %10
        num = int(num /10)
        tens = num %10
        num = int(num /10) 
        hundreds = num %10
        num = int(num /10) 
        thousands = num %10
        ans = ""
        str1000 = ""
        for i in range (thousands):
            str1000+= "M"
        str100 = ""    
        if(hundreds == 9):
            str100 = "CM"
        elif(hundreds == 4):
            str100 = "CD"
        elif(hundreds == 6):
            str100 = "DC"    
            
        elif(hundreds <= 4):
            for i in range (thousands):
                str1000+= "M"
        else:
           str100 = "D"
               
        
def main():
    height = num = 3
    object = Solution()
    print(object.intToRoman(height))


if __name__ == "__main__":
    main()   