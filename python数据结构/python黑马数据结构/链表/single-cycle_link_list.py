"""重要的就是要考虑周全，普通情况和特殊情况"""
class SingleNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class CycleLinkList(object):
    """循环单链表"""

    def __init__(self, node=None):
        if node:
            node.next = node
        self.head = node

    def is_empty(self):
        """链表是否为空"""
        return self.head == None

    def length(self):
        """链表长度"""
        if self.head is None:
            return 0
        cur = self.head
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
        while cru != None and cru.next != self.head:
            if cru.item == item:
                return True
            cru = cru.next
        if cru.item == item:
            return True
        return False

    def add(self, item):
        """链表头部添加元素"""
        node = SingleNode(item)
        if self.is_empty():
            self.head = node
            node.next = node

        node.next = self.head
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        cur.next = node
        self.head = node

    def append(self, item):
        """链表尾部添加元素"""
        cur = self.head
        if cur is None:
            self.add(item)
        else:
            while cur.next != self.head:
                cur = cur.next
            node = SingleNode(item)
            node.next = self.head
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            # 如果是中间插入那么和普通单链表没有区别
            node = SingleNode(item)
            cur = self.head
            count = 0
            while count < (pos - 1):
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除节点"""
        # 将每一个节点的值拿出来进行比对，如果相同，执行删除操作，如果判断完所有数据都没有相同，什么都不做
        # 特殊情况
        cru = self.head
        remove_one_node = False
        if cru is None:
            return
        while cru.next != self.head:
            # 要删除的是首节点
            if cru.item == item:
                if cru.next == self.head:
                    # 只有一个节点
                    self.head = None
                else:
                    # 移除首节点
                    remove_one_node = True
                break

            if cru.next:
                if cru.next.item == item:
                    if cru.next.next == self.head:
                        # 移除尾节点
                        cru.next = self.head
                    else:
                        # 移除中间
                        cru.next = cru.next.next
                    break
            cru = cru.next
        if remove_one_node:
            # 移除首节点
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = cur.next


if __name__ == "__main__":
    ll = CycleLinkList()
    # print(ll.search('aaa'))
    #
    # print(ll.is_empty())
    # print(ll.length())

    ll.append(1)
    # print(ll.search(2), '是否存在')
    # ll.append(2)
    # ll.append(3)
    # ll.append(5)
    # ll.append(6)
    # ll.insert(0, 0)
    # ll.insert(4, 4)
    # print(ll.travel(), '遍历')
    ll.remove(1)
    ll.travel()
    # print(ll.is_empty(),'是否为空')
    # print(ll.length(), '长度')
    # print(ll.travel(), '遍历')
    # ll.remove(6)
    # ll.insert(6,6)
    # print(ll.search(6), '是否存在')
    # print(ll.travel(), '遍历')
    # ll.remove(1)
    # ll.remove(1)
    # ll.remove(1)
    # ll.remove(52)
    # ll.append(2)
    # ll.append(3)
    #
    #
    # ll.travel()
    #
    # ll.append(4)
    # ll.append(5)
    # ll.append(6)
    # ll.remove(6)
    # ll.travel()
    # print(ll.length())
    #
    # ll.remove(3)
    # ll.travel()
    # print(ll.length())
