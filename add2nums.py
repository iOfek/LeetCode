# Definition for singly-linked list.
from decimal import ROUND_DOWN
import math


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
   
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode()
        node3 = l3
        node1 = l1
        node2 = l2
        carry =0
        while True:
            # sum = ((node1.val if (node1.val is not None) else 0)  + (node2.val if (node2.val is not None) else 0  ))
            sum = carry + node1.val + node2.val
            node3.val += sum%10
            carry = int(math.floor(sum/10))
            if(node3.val == 10):
                node3.val =0
            if ((node1.next is  None) and (node2.next is  None)):
                break   
            node1= node1.next if (node1.next is not None) else ListNode()
            node2= node2.next if (node2.next is not None) else ListNode()
            if(node3.next is None):
                node3.next = ListNode()
            node3 = node3.next
        if(carry > 0):
            node3.next =ListNode(carry) 
        
        # sum = ((node1.val if (node1.val is not None) else 0)  + (node2.val if (node2.val is not None) else 0  ))
        # node3.val += sum%10; 
        # if sum > 9:
        #     node3.next = ListNode(1)
            
        return l3
    
    
def main():
    l1 = ListNode(2,ListNode(4,ListNode(3)))
    l2 = ListNode(5,ListNode(6,ListNode(4)))
    # l1 = ListNode()
    # l2 = ListNode()
    object = Solution();
    l3 = object.addTwoNumbers(l1,l2)
    print (l3.val,l3.next.val,l3.next.next.val )
    # print (l3.val )


if __name__ == "__main__":
    main()
        