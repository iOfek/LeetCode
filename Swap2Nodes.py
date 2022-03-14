# Definition for singly-linked list.
from gc import set_debug


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if no pair return original
        if head is None or head.next is None:
            return head
        # first Swap
        
        first = head
        second = head.next
        temp = second.next
        first.next = temp
        second.next = first
        new_head = second
        # rename for clarity
        temp = first
        first = second 
        second = temp      
        # check if possible advance
        while second.next is not None and second.next.next is not None:
            originalSecond = second
            second = second.next.next
            first = first.next.next
            temp = second.next
            first.next = temp
            second.next = first
            # rename for clarity
            temp = first
            first = second 
            second = temp
            
            originalSecond.next = first
            
        return new_head 
       
def main():
    object = Solution()
    list = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
    object.swapPairs(list)
    print (list)
   

if __name__ == "__main__":
    main() 