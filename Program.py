from BSTree import BinarySearchTree as BST
from LinkedList import LinkedList as LL



tree = BST()
tree.insert(50).insert(30).insert(20).insert(40).insert(10).insert(70).insert(60).insert(80).insert(90)
print(tree.preOrder.__doc__)
tree.preOrder()

linkedlist = LL()
linkedlist.append(12).append(20).append(3).append(7).append(19).append(35).append(1).append(44)
print(linkedlist)

linkedlist.reverse()
print(linkedlist)