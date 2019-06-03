# Linked List Class

#List Node Class
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    def __str__(self):
        return f'{self.val}'

class LinkedList:
    def __init__(self):
        self.head:ListNode = None
    
    def __repr__(self):
        printer = ""
        nodeToPrint = self.head

        while(nodeToPrint):
            printer += f'{nodeToPrint.val}'
            if nodeToPrint.next != None:
                printer += "->"
            nodeToPrint = nodeToPrint.next
        
        return printer

    # Appends a node to the end of the linked list
    def append(self, val):
        if(self.head == None):
            self.head = ListNode(val)
            return self
        
        runner = self.head
        # Moving runner to the end of the list
        while runner.next:
            if runner.val == val:
                return self.head
            runner = runner.next
    
        runner.next = ListNode(val)

        return self        

    # deletes a node from the linked list
    def remove(self, val):
        if(self.head == None):
            return self
        
        if(self.head.val == val):
            temp = self.head.next
            self.head.next = None
            self.head = temp
            return self

        prev = self.head
        curr = self.head.next

        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr.next = None
                return self

            curr = curr.next
            prev = prev.next

        return self
    
    #reverse the linked list
    def reverse(self):
        if self.head.next == None:
            return self

        prev = None
        curr = self.head

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        # list head is now the last node
        self.head = prev

        return self

    # Detects a circle within the linked list
    def detectCircle(self):
        if self.head == None or self.head.next == None or self.head.next.next == None:
            return False
        
        fast = self.head
        slow = self.head

        while slow and fast:
            if fast.next == None:
                return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow.next:
                return True

        return False

    # Creates a circle in the linked list
    def createCircle(self):
        if self.head == None or self.head.next == None:
            return self
        
        tail = self.head

        while tail.next:
            tail = tail.next
        
        tail.next = self.head.next
