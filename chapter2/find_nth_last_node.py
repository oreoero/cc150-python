'''
Created on Apr 7, 2016
Implement an algorithm to find the nth to last element of a singly linked list.

@author: chunq
'''

from objects.LinkedList import LinkedList
from objects.LinkedNode import LinkedNode

class AdvancedLinkedList(LinkedList):

    def findNthLastNode(self,distant):
        first = self.head
        second = self.head
        while distant >= 0:
            distant -= 1
            if first is None:
                return None
            else:
                first = first.next
        
        while first is not None:
            first = first.next
            second = second.next
        
        return second

if __name__ == "__main__":
    testList = AdvancedLinkedList()
    testList.append(LinkedNode(4))
    testList.append(LinkedNode(3))
    testList.append(LinkedNode(2))
    testList.append(LinkedNode(1))
    print(testList.findNthLastNode(1).data)
    
            
        
            
        