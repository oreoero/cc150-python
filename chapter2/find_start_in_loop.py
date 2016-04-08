'''
Created on Apr 7, 2016
Given a circular linked list, implement an algorithm which returns node at the beginning of the loop.
@author: chunq
'''

from objects.LinkedList import LinkedList

def findStartNodeInLoop(testList):
    fastRunner = testList.head
    slowRunner = testList.head
    
    while (fastRunner != slowRunner):
        if (fastRunner.next is None ) or (slowRunner is None):
            return None
        slowRunner = slowRunner.next
        fastRunner = fastRunner.next.next
        
    fastRunner = testList.head
    while (fastRunner != slowRunner):
        fastRunner = fastRunner.next
        slowRunner = slowRunner.next
    
    return fastRunner
    