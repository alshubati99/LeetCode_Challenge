class ListNode:
    def __init__(self,val=0, next =None):
        self.val=val # the value of the node 
        self.next=next # A pointer to the next node 
#This class will is used to create the constrcutors which are the nodes in the linked list

class Solution:
    def reversebtihalsList( self, head:ListNode)-> ListNode: #takes the linked list head as input and returns a new head 
        if not head or not head.next: #the final node is reached or the list is empty 
            return head #return the new head
        nhead=self.reversebtihalsList(head.next)#the function keeps calling itself recursively till it reaches the base case
        head.next.next=head #reverse the link
        head.next=None #break the old link as it is pointless
        return nhead #return the last node which is now the newhead after reversing the list
    #lets create a function to test this with

def create_linked_list(vals):#this function takes the values as inputs
        if not vals:
            return None
        head =ListNode(vals[0])
        current =head

        for v in vals[1:]:
            current.next=ListNode(v)
            current=current.next

        return head 
    
def print_linked_list(head):
        current= head
        while current:
            print(current.val,end= " - > ")
            current =current.next

        print("None")
    
if __name__=="__main__":
        values=[1,2,3,4,5]
        head = create_linked_list(values)

        print("original")
        print_linked_list(head)
        sol= Solution()
        reversedhead=sol.reversebtihalsList(head)

        print("after")
        print_linked_list(reversedhead)


