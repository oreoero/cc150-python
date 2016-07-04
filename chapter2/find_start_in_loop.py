'''
Created on Apr 7, 2016
Given a circular linked list, implement an algorithm which returns node at the beginning of the loop.
@author: chunq
'''

from objects.LinkedNode import LinkedNode
from objects.LinkedList import LinkedList

def findStartNodeInLoop(testList):
    fastRunner = testList.head
    slowRunner = testList.head
    
    while fastRunner.next:
        slowRunner = slowRunner.next
        fastRunner = fastRunner.next.next
        if fastRunner == slowRunner:
            break
    
    if fastRunner == None:
        return None
        
    fastRunner = testList.head
    while (fastRunner != slowRunner):
        fastRunner = fastRunner.next
        slowRunner = slowRunner.next
    
    return fastRunner

if __name__ == "__main__":
    testList = LinkedList()
    testNode3 = LinkedNode(3)
    testNode6 = LinkedNode(6)
    testList.append(testNode6)
    testList.append(LinkedNode(5))
    testList.append(LinkedNode(4))
    testList.append(testNode3)
    testList.append(LinkedNode(2))
    testList.append(LinkedNode(1))
    testNode6.next = testNode3
    print(findStartNodeInLoop(testList).data)
    