"""重要的就是要考虑周全，普通情况和特殊情况"""
class BaseLinkList(object):
    """链表基板"""

    def is_empty(self):
        """链表是否为空"""
        return self.head == None

    def length(self):
        """链表长度"""
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.head
        if cur is None:
            return cur
        print('- ', end='')
        while cur:
            print(cur.item, end=',')
            cur = cur.next
        print(' -')

    def search(self, item):
        """查找节点是否存在"""
        # 将每一个节点的值拿出来进行比对，如果找到，返回true如果没有找到返回false
        cru = self.head
        while cru != None:
            if cru.item == item:
                return True
            cru = cru.next
        return False


class SingleNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(BaseLinkList):
    """单链表"""

    def __init__(self, node=None):
        self.head = node

    def add(self, item):
        """链表头部添加元素"""
        node = SingleNode(item)
        node.next = self.head
        self.head = node

    def append(self, item):
        """链表尾部添加元素"""
        cur = self.head
        if cur == None:
            node = SingleNode(item)
            self.head = node
        else:
            while cur.next:
                cur = cur.next
            node = SingleNode(item)
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
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
        while cru != None:
            # 只有一个节点
            if cru.item == item:
                self.head = cru.next
                break

            if cru.next:
                if cru.next.item == item:
                    cru.next = cru.next.next
                    break
            cru = cru.next

    def is_loop(self):
        """
        判断是否有环路
        解题思想1：分出两个指针一个指针P每次前进一，后一个指针PP，然后有一个计数器，
        P每走一步，计数器加1，PP指针每次从头来走，走到P的前一个步长停
        结论：如果没有环路，那么循环正常退出，如果有环路PP指针一定会和P指针重合,有重合返回True

        参考文档：https://zhuanlan.zhihu.com/p/31401474

        """
        cur = self.head.next
        # 1, 1, 1, 2, 1, 2
        # 0, 0, 1, 1
        count = 1
        while cur is not None:
            is_cur = self.head
            for i in range(count):
                if cur == is_cur:
                    return True
                is_cur = is_cur.next
            cur = cur.next
            count += 1
        return False


if __name__ == "__main__":
    ll = SingleLinkList()
    ll.append(1)
    ll.append(1)
    ll.append(1)
    ll.append(2)
    ll.append(1)
    ll.append(2)
    # ll.head.next = ll.head
    # ll.head.next.next.next.next = ll.head.next
    print(ll.is_loop())

