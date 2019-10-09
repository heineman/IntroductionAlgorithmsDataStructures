"""
    AVL Implementation of Binary Tree.

    Implementation taken from

    https://github.com/heineman/python-data-structures
    
"""

class BinaryNode:

    def __init__(self, value = None):
        """Create binary node."""
        self.value  = value
        self.left   = None
        self.right  = None
        self.height = 0

    def computeHeight(self):
        """Compute height of node in BST."""
        height = -1
        if (self.left):
            height = max(height, self.left.height)
        if (self.right):
            height = max(height, self.right.height)
            
        self.height = height + 1

    def dynamicHeight(self):
        """Compute height of node in BST."""
        height = -1
        if (self.left):
            height = max(height, self.left.dynamicHeight())
        if (self.right):
            height = max(height, self.right.dynamicHeight())
            
        return height + 1

    def dynamicHeightDifference(self):
        """Compute height difference of node's children in BST."""
        leftTarget = 0
        rightTarget = 0
        if (self.left):
            leftTarget = 1 + self.left.dynamicHeight()
        if (self.right):
            rightTarget = 1 + self.right.dynamicHeight()
            
        return leftTarget - rightTarget

    def heightDifference(self):
        """Compute height difference of node's children in BST."""
        leftTarget = 0
        rightTarget = 0
        if (self.left):
            leftTarget = 1 + self.left.height
        if (self.right):
            rightTarget = 1 + self.right.height
            
        return leftTarget - rightTarget

    def assertAVLProperty(self):
        """Validate AVL property for BST node."""
        if abs(self.dynamicHeightDifference()) > 1:
            return False
        if (self.left):
            if not self.left.assertAVLProperty():
                return False
        if (self.right):
            if not self.right.assertAVLProperty():
                return False

        return True

    def rotateRight(self):
        """Perform right rotation around given node."""
        newRoot = self.left
        grandson = newRoot.right
        self.left = grandson
        newRoot.right = self

        self.computeHeight()
        return newRoot

    def rotateLeft(self):
        """Perform left rotation around given node."""
        newRoot = self.right
        grandson = newRoot.left
        self.right = grandson
        newRoot.left = self
    
        self.computeHeight()
        return newRoot

    def rotateLeftRight(self):
        """Perform left, then right rotation around given node."""
        child = self.left
        newRoot = child.right
        grand1  = newRoot.left
        grand2  = newRoot.right
        child.right = grand1
        self.left = grand2
    
        newRoot.left = child
        newRoot.right = self
    
        child.computeHeight()
        self.computeHeight()
        return newRoot

    def rotateRightLeft(self):
        """Perform right, then left rotation around given node."""
        child = self.right
        newRoot = child.left
        grand1  = newRoot.left
        grand2  = newRoot.right
        child.left = grand2
        self.right = grand1
    
        newRoot.left = self
        newRoot.right = child
    
        child.computeHeight()
        self.computeHeight()
        return newRoot

    def add(self, val):
        """Adds a new node to the tree with value and Rebalance as needed."""
        newRoot = self
        
        if val <= self.value:
            self.left = self.addToSubTree(self.left, val)
            if self.heightDifference() == 2:
                if val <= self.left.value:
                    newRoot = self.rotateRight()
                else:
                    newRoot = self.rotateLeftRight()
        else:
            self.right = self.addToSubTree(self.right, val)
            if self.heightDifference() == -2:
                if val > self.right.value:
                    newRoot = self.rotateLeft()
                else:
                    newRoot = self.rotateRightLeft()

        newRoot.computeHeight()
        return newRoot

    def addToSubTree(self, parent, val):
        """Add val to parent subtree (if exists) and return root of that subtree."""
        if parent is None:
            return BinaryNode(val)

        parent = parent.add(val)
        return parent
           
    def removeFromParent(self, parent, val):
        """Helper method for remove. Ensures proper behavior when removing node that 
        has children."""
        if parent:
            return parent.remove(val)
        return None

    def remove(self, val):
        """
         Remove val of self from BinaryTree. Works in conjunction with remove
         method in BinaryTree.
        """
        newRoot = self
        if self.value == val:
            if self.left is None:
                return self.right

            child = self.left
            while child.right:
                child = child.right
            
            childKey = child.value;
            self.left = self.removeFromParent(self.left, childKey)
            self.value = childKey;

            if self.heightDifference() == -2:
                if self.right.heightDifference() <= 0:
                    newRoot = self.rotateLeft()
                else:
                    newRoot = self.rotateRightLeft()
        elif self.value > val:
            self.left = self.removeFromParent(self.left, val)
            if self.heightDifference() == -2:
                if self.right.heightDifference() <= 0:
                    newRoot = self.rotateLeft()
                else:
                    newRoot = self.rotateRightLeft()
        else:
            self.right = self.removeFromParent(self.right, val)
            if self.heightDifference() == 2:
                if self.left.heightDifference() >= 0:
                    newRoot = self.rotateRight()
                else:
                    newRoot = self.rotateLeftRight()

        newRoot.computeHeight()
        return newRoot

    def __repr__(self):
        """Useful debugging function to produce linear tree representation."""
        leftS = ''
        rightS = ''
        if self.left:
            leftS = str(self.left)
        if self.right:
            rightS = str(self.right)
        return "(L:" + leftS + " " + str(self.value) + " R:" + rightS + ")"

    def inorder(self):
        """In order traversal generator of tree rooted at given node."""
        if self.left:
            for v in self.left.inorder():
                yield v

        yield self.value

        if self.right:
            for v in self.right.inorder():
                yield v

class BinaryTree:

    def __init__(self):
        """Create empty binary tree."""
        self.root = None

    def __str__(self):
        if self.root:
            return str(self.root)
        
    def add(self, value):
        """Insert value into proper location in Binary Tree."""
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root = self.root.add(value)

    def __contains__(self, target):
        """Check whether BST contains target value."""
        node = self.root
        while node:
            if node.value == target:
                return True
            elif node.value > target:
                node = node.left
            else:
                node = node.right
                
        return False

    def remove(self, val):
        """Remove value from tree."""
        if self.root:
            self.root = self.root.remove(val)

    def __iter__(self):
        """In order traversal of elements in the tree."""
        if self.root:
            for e in self.root.inorder():
                yield e
                
    def assertAVLProperty(self):
        """Validate AVL property for BST Tree."""
        if self.root:
            return self.root.assertAVLProperty()
        return True

    def __repr__(self):
        if self.root is None:
            return "avl:()"
        return "avl:" + str(self.root)
