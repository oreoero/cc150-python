'''
Created on Apr 7, 2016

@author: chunq
'''
from objects.LinkedNode import LinkedNode
from objects.LinkedList import LinkedList

if __name__ == "__main__":
    testList = LinkedList()
    testList.append(LinkedNode(3))
    testList.append(LinkedNode(4))
    testList.append(LinkedNode(5))
    testList.view()
    testList.remove(LinkedNode(4))
    testList.view()
    testList.remove(LinkedNode(1))
    testList.view()
    testList.remove(LinkedNode(5))
    testList.view()
    testList.remove(LinkedNode(3))
    testList.view()
    testList.remove(LinkedNode(3))
    testList.view()
    print(testList.count)