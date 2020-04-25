class Deque(object):
    """双端队列"""
    def __init__(self):
        self._deque = []

    def is_empty(self):
        """判断队列是否为空"""
        return not self._deque

    def add_front(self, item):
        """在队头添加元素"""
        self._deque.append(0)

    def add_rear(self, item):
        """在队尾添加元素"""
        self._deque.append()

    def remove_front(self):
        """从队头删除元素"""
        self._deque.pop(0)

    def remove_rear(self):
        """从队尾删除元素"""
        self._deque.pop()

    def size(self):
        """返回队列大小"""
        return len(self._deque)