#
# @lc app=leetcode.cn id=707 lang=python
#
# [707] 设计链表
#

# @lc code=start
class ListNode:
    def __init__(self, v):
        self.v = v
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(0)
        self.length = 0


    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index > self.length - 1:
            return -1

        tmp = self.head
        for _ in range(0, index):
            tmp = tmp.next
        return tmp.next.v




    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        t = self.head.next
        self.head.next = ListNode(val)
        self.head.next.next = t
        self.length += 1

        


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = ListNode(val)
        self.length += 1


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.length:
            return 
        tmp = self.head
        for _ in range(0, index):
            tmp = tmp.next
        t = tmp.next
        tmp.next = ListNode(val)
        tmp.next.next = t
        self.length += 1




    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index > self.length - 1:
            return 
        tmp = self.head
        for _ in range(0, index):
            tmp = tmp.next
        tmp.next = tmp.next.next
        self.length -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

