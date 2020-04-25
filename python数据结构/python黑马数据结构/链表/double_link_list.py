"""重要的就是要考虑周全，普通情况和特殊情况"""
from python数据结构.python黑马数据结构.链表.single_link_list import BaseLinkList


class Node:
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None


class DoubleLinkList(BaseLinkList):
    """双链表"""
    def __init__(self, node=None):
        self.head = node


    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.head
        self.head = node
        node.prev = None

    def append(self, item):
        """链表尾部添加元素"""
        cur = self.head
        if cur == None:
            node = Node(item)
            self.head = node
        else:
            while cur.next:
                cur = cur.next
            node = Node(item)
            cur.next = node
            node.prev = cur
            node.next = None

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            node = Node(item)
            cur = self.head
            count = 0
            while count <= pos:
                cur = cur.next
                count += 1
            node.prev = cur.prev
            node.next = cur
            node.prev.next = node
            node.next.prev = node

    def remove(self, item):
        """删除节点"""
        # 将每一个节点的值拿出来进行比对，如果相同，执行删除操作，如果判断完所有数据都没有相同，什么都不做
        # 特殊情况
        cru = self.head
        while cru != None:
            # 只有一个节点
            if cru.item == item:
                if cru == self.head:
                    self.head = cru.next
                    if self.head:
                        self.head.prev = cru.prev
                    break
                else:
                    cru.prev.next = cru.next
                    if cru.next:
                        cru.next.prev = cru.prev
                    break
            else:
                cru = cru.next


if __name__ == "__main__":
    ll = DoubleLinkList()
    # ll.add(1)
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.remove(1)
    ll.remove(4)
    ll.remove(5)
    ll.remove(5)
    # ll.remove(2)
    # ll.remove(3)

    ll.travel()
