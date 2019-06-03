# This class is my implementation of a binary search tree

# Binary Search Tree Node
class BSTNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def inOrder(self):
        """Prints the tree using inorder traversal."""  
        self._inOrderPrint(self.root)
        return self

    def _inOrderPrint(self, node: BSTNode):
        if node:
            self._inOrderPrint(node.left)
            print(node.val)
            self._inOrderPrint(node.right)
        return self

    def preOrder(self):
        """Prints the tree using preorder traversal."""  
        self._preOrderPrint(self.root)
        return self

    def _preOrderPrint(self, node: BSTNode):
        if node:
            print(node.val)
            self._preOrderPrint(node.left)
            self._preOrderPrint(node.right)
        return self
    
    def postOrder(self):
        """Prints the tree using postorder traversal."""  
        self._postOrderPrint(self.root)
        return self
    
    def _postOrderPrint(self, node: BSTNode):
        if node:
            self._postOrderPrint(node.left)
            self._postOrderPrint(node.right)
            print(node.val)
        return self

    def insert(self, val: int):
        """Inserts the value into the tree."""  
        if not self.root:
            self.root = BSTNode(val)
            return self

        # Pointer at top of list    
        currNode = self.root

        while(currNode):
            if val > currNode.val:
                if currNode.right:
                    currNode = currNode.right
                else:
                    currNode.right = BSTNode(val)
                    return self
            elif val < currNode.val:
                if currNode.left:
                    currNode = currNode.left
                else:
                    currNode.left = BSTNode(val)
                    return self
            else:
                return self

    def deleteNode(self, val: int):
        """Deletes the given value node from the tree."""  
        self._remove(val, self.root)
        return self

    def _remove(self, val: int, node: BSTNode):
        if not node:
            return self

        # Node to delete is on the left
        if val < node.val:
            node.left = self._remove(val, node.left)
        # Node to delete is to the right
        elif val > node.val:
            node.right = self._remove(val, node.right)
        # Found the Node to delete
        else:
            # if no left sub tree, then replace with right sub tree 
            if not node.left:
                temp = node.right
                node = None
                return temp
            # if no right sub tree, then replace with left sub tree 
            elif not node.right:
                temp = node.left
                node = None
                return temp
            
            # replace node with next biggest node
            temp = self.minValueNode(node.right)
            node.val = temp.val
            node.right = self._remove(node.val, node.right)
        return node

    
    def minValueNode(self, node: BSTNode) -> BSTNode:
        """Returns the smallest value node attached to the given node."""  
        current = node
        while current.left:
            current = current.left
        
        return current

    def search(self, val: int) -> BSTNode:
        """Returns the node if it exist in the tree otherwise returns None."""  
        return self._find(self.root, val)

    def _find(self, node: BSTNode, val: int) -> BSTNode:
        if not node:
            return None
        if val < node.val:
            return self._find(node.left, val)
        elif val > node.val:
            return self._find(node.right, val)
        else:
            return node