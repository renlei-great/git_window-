"""重要的就是要考虑周全，普通情况和特殊情况"""
class BaseLinkList(object):
    """链表基板"""

    def is_empty(self):
        """链表是否为空"""
        return self.head is None

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

    def reverse_index(self, index):
        """查看倒数第index 的数是什么"""
        try:
            if self.is_empty():
                return None

            le = self.length()
            n = le - index
            if n >= 0:
                cur = self.head
                for i in range(n):
                    cur = cur.next
                return cur.item
            else:
                return None
        except AttributeError:
            return None

    def reverse_star_end(self):
        """反转第一个和最后一个节点"""
        if self.head and self.head.next:
            cur_p = self.head
            cur_n = self.head.next
            # 找到前一个和最后一个节点
            while cur_n.next:
                cur_p = cur_n
                cur_n = cur_n.next

            if self.length() == 2:
                cur_p.next = None
                cur_n.next = cur_p
                self.head = cur_n
            else:
                cur_n.next = self.head.next
                cur_p.next = self.head
                self.head.next = None
                self.head = cur_n
        else:
            pass

    def reverse(self):
        """反转列表
        单链表反转的思想：
            1. 创建一个新列表
            2. 从旧链表中依次往出取数据
            3. 然后将这个数据每次都插入到新列表的头部
            4. 反转完成
        """
        if self.head.next is None:
            return

        cur = self.head
        ll = SingleLinkList()
        while True:
            cur = self.head
            if cur is None:
               break
            ll.add(self.head.item)
            self.head = self.head.next
        self.head = ll.head

    def reverse_print(self):
        """反向输出"""

        if self.head is None:
            return

        cur = self.head
        stack = list()
        while cur is not None:
            """遍历每个节点，压入在中，这里用列表实现栈的功能"""
            stack.insert(0, cur.item)
            cur = cur.next

        for item in stack:
            print(item, end=" ")

    def pop(self):
        """弹出头结点位置的元素"""
        if self.head is None:
            return None

        ret = self.head.item
        self.head = self.head.next
        return ret

def merge_single(l1:SingleLinkList, l2:SingleLinkList):
    """合并两个有序集合"""
    if l1.is_empty() and l2.is_empty():
        """对两个链表进行判空"""
        return

    new_l = SingleLinkList()
    l1_val = l1.pop()
    l2_val = l2.pop()
    while l1_val is not None and l2_val is not None:
        if int(l1_val) <= int(l2_val):
            new_l.append(l1_val)
            l1_val = l1.pop()
        else:
            new_l.append(l2_val)
            l2_val = l2.pop()
    if not l1.is_empty():
        l1_val = l1.pop()
        while l1_val is not None:
            new_l.append(l1_val)
            l1_val = l1.pop()
    elif not l2.is_empty():
        l2_val = l2.pop()
        while l2_val is not None:
            new_l.append(l2_val)
            l2_val = l2.pop()
    return new_l


if __name__ == "__main__":
    l1 = SingleLinkList()
    l1.append(1)
    l1.append(5)
    l1.append(9)
    l1.append(15)
    l1.append(26)
    l1.append(32)

    l2 = SingleLinkList()
    l2.append(2)
    l2.append(7)
    l2.append(16)
    l2.append(17)
    l2.append(21)
    l2.append(34)
    new_l = merge_single(l1, l2)
    new_l.travel()





