# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        left=list1
        right=list2
        dummy=ListNode(0)
        newnode=dummy
        while left and right :
            if left.val<right.val:
                newnode.next=left
                left=left.next
                newnode=newnode.next
            else:
                newnode.next=right
                right=right.next
                newnode=newnode.next
        if left:
            newnode.next=left
           
        else :
            newnode.next=right
                      
        return dummy.next
         

        
        