# Definition for singly-linked list.
from matplotlib.pyplot import step


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if not head or not head.next or k ==0:
            return head
        first = head
        curr = head
        length = 1
        while curr.next:
            length +=1
            curr= curr.next
        rotations = k % length
        if k % length == 0:
            return head
        steps = length - rotations-1
        curr = first
        for i in range (steps):
            curr = curr.next
        newHead = curr.next
        curr.next =None
        curr = newHead
        while curr.next:
            curr = curr.next
        curr.next = first
        return newHead
        
def main():
    object = Solution()
    list = ListNode(1,ListNode(2,ListNode(3)))
    k=20000000
    new_list = object.rotateRight(list,k)
    curr= new_list
    while curr:
        print (curr.val)
        curr = curr.next

if __name__ == "__main__":
    main()     