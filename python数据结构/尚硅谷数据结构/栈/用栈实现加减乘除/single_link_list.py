"""重要的就是要考虑周全，普通情况和特殊情况"""
from python数据结构.python黑马数据结构.链表.single_link_list import BaseLinkList


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

    def pop(self):
        """弹出头结点位置的元素"""
        if self.head is None:
            return None

        ret = self.head.item
        self.head = self.head.next
        return ret

    def peep(self):
        if self.head is None:
            return None

        ret = self.head.item
        return ret


if __name__ == "__main__":
    pass





