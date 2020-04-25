"""重要的就是要考虑周全，普通情况和特殊情况"""

class Node:
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None


class DoubleCycleLinkList(object):
    """双链表"""
    def __init__(self, node=None):
        if node:
            node = self.__add_none_node(node)
        self.head = node

    def __add_none_node(self, node):
        """为空链表创建一个node,只适用于给空链表创建一个节点"""
        if self.is_empty():
            node = Node(node)
            node.next, node.prev = node, node
            self.head = node
            return node
        raise TypeError('这不是一个空链表')

    def is_empty(self):
        """链表是否为空"""
        return self.head is None

    def length(self):
        """链表长度"""
        cur = self.head
        if self.is_empty():
            return 0
        count = 1
        while cur.next != self.head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.head
        if cur is None:
            return cur
        print('- ', end='')
        while cur.next != self.head:
            print(cur.item, end=',')
            cur = cur.next
        print(cur.item, end=',')
        print(' -')

    def search(self, item):
        """查找节点是否存在"""
        # 将每一个节点的值拿出来进行比对，如果找到，返回true如果没有找到返回false
        cru = self.head
        while cru.next != self.head:
            if cru.item == item:
                return True
            cru = cru.next
        if cru.item == item:
            return True
        return False

    def add(self, item):
        """链表头部添加元素"""
        cur = self.head
        if cur is None:
            self.__add_none_node(item)
        else:
            # 找到最后一个元素
            while cur.next != self.head:
                cur = cur.next
            node = Node(item)
            node.next = self.head
            self.head = node
            node.prev = cur
            cur.next = node

    def append(self, item):
        """链表尾部添加元素"""
        cur = self.head
        if cur is None:
            self.__add_none_node(item)
        else:
            while cur.next != self.head:
                cur = cur.next
            node = Node(item)
            node.prev = cur
            node.next = cur.next
            node.next.prev = node
            node.prev.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0 or self.head is Node:
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
        if cru is None:
            return
        while cru.next != self.head:
            # 第一个节点就是
            if cru.item == item:
                cru.next.prev = cru.prev
                cru.next.prev.next = cru.next
                self.head = cru.next
                return
            # 不是第一个节点
            if cru.next.item == item:
                if cru.next.next == self.head:
                    # 最后一个节点
                    cru.next = self.head
                    cru.next.prev = cru
                else:
                    # 中间节点
                    cru.next = cru.next.next
                    cru.next.prev = cru
                return
            cru = cru.next
        if cru.next == self.head and cru.item == item:
            # 只有一个节点,并且要移除
            self.head = None


if __name__ == "__main__":
    ll = DoubleCycleLinkList()
    # ll.add(1)
    ll.append(1)
    ll.append(2)
    # ll.append(3)
    # ll.append(4)
    # ll.append(5)
    # ll.remove(1)
    # ll.remove(2)
    # ll.travel()
    # ll.remove(3)
    # ll.travel()
    # ll.remove(4)
    # ll.travel()
    # ll.remove(4)
    #
    # ll.travel()
    ll.remove(1)

    ll.travel()
