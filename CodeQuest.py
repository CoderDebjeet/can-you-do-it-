# Welcome to the Lumos Coding Quest
# you have been given a linked list with duplicate values
# upon running this code, you will see a string that has been formed by collecting the data in the nodes of the linked list
# you need to complete the "MyAnswer" function and ensure that it removes the duplicate nodes from the linkedlist
# when you collate the string that this new linked list contains, you will get the link to the whitelist form

# Note:- "list" represents the said linked list

from helper import *


def MyAnswer(self):
    ptr1 = None
        ptr2 = None
        dup = None
        ptr1 = self.head
 
        # Pick elements one by one
        while (ptr1 != None and ptr1.next != None):
 
            ptr2 = ptr1
 
            # Compare the picked element with rest
            # of the elements
            while (ptr2.next != None):
 
                # If duplicate then delete it
                if (ptr1.data == ptr2.next.data):
 
                    # Sequence of steps is important here
                    dup = ptr2.next
                    ptr2.next = ptr2.next.next
                else:
                    ptr2 = ptr2.next
 
            ptr1 = ptr1.next
 
   answer = ""
   print(answer)


MyAnswer(list)




