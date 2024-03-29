'''
Created on Apr 19, 2016

@author: chunq
'''

class BST(object):
    def __init__(self):
        self.root = None
    
    def insert(self, newKey):
        newNode = BSTNode(newKey)
        if self.root:
            self.root.insert(newKey)      
        else:
            self.root = newNode
            newNode.parent = self.root      
    
    def find(self, targetKey):
        if self.root:
            return self.root.find(targetKey)
        else:
            return None
        
    def delete(self, keyToDelete):
        nodeToDelete = self.find(keyToDelete)
        if nodeToDelete:
            nodeToDelete.delete()
    
    def __str__(self):
        if self.root is None: return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent and \
               node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
              [left_line + ' ' * (width - left_width - right_width) +
               right_line
               for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self.root) [0])
    
class BSTNode(object):
    '''
    Representation of a binary search tree node
    Property: 
            key, a left child, a right child, a parent node
    Method: search/insert/delete a value in its subtree
            view subTree
    '''

    def __init__(self, key):
        '''
        creation of a BST node pointing to nowhere
        '''
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
    
    def __repr__(self):
        return str(self.key)
        
    def find(self, targetKey):
        '''
        return the node that contains the target key
        '''
        if targetKey == self.key:
            return self
        elif targetKey < self.key:
            if self.left:
                return self.left.find(targetKey)
            else:
                return None
        else:
            if self.right:
                return self.right.find(targetKey)
            else:
                return None
    
    def insert(self, newKey):
        '''
        doesn't allow duplicate
        '''
        if newKey == self.key:
            return
        elif newKey < self.key:
            if self.left:
                self.left.insert(newKey)
            else:
                newNode = BSTNode(newKey)
                self.left = newNode
                newNode.parent = self
        else:
            if self.right:
                self.right.insert(newKey)
            else:
                newNode = BSTNode(newKey)
                self.right = newNode
                newNode.parent = self
                
    def delete(self):
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                self.parent.left.parent = self.parent
            else:
                self.parent.right = self.right or self.right
                self.parent.right.parent = self.parent
        else:
            transplantNode = self.right.minimum()
            self.key = transplantNode.key
            transplantNode.delete()
            
    def successor(self):
        '''
        return the node that contains the next largest number in the subtree
        '''
        if self.right:
            return self.right.minimum()
        else:
            searchNode = self
            while searchNode and searchNode == searchNode.parent.left:
                searchNode = searchNode.parent
            return searchNode          
    
    def minimum(self):
        '''
        According to BST's property, the left most leave in the subtree is the minimum
        return the reference to the minimum node, not the value
        '''
        if self.left:
            return self.left.minimum()
        else:
            return self

if __name__ == '__main__':
    
    testTree = BST()
    testTree.insert(5)
    testTree.insert(2)
    testTree.insert(12)
    testTree.insert(-4)
    testTree.insert(3)
    testTree.insert(9)
    testTree.insert(21)
    testTree.insert(19)
    testTree.insert(20)
    testTree.insert(25)
    print(testTree)
    testTree.delete(12)
    print(testTree)
        
        