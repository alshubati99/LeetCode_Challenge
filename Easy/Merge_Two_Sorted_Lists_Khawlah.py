
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
        # create a dummy node to serve as the start of the merged list
        dummy = ListNode()
        current = dummy # pointer to track the last node in hte merged list

        # traverse both lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next # move to next node

        # attach the remaining node
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        # return the merged list
        return dummy.next

    
"""
Time Complexity: O(N+M), where N and M are the lengths of list1 and list2. Each node is visited once.
Space Complexity: O(1), since we modify the lists in place without extra storage.

"""