class Queue(object):
    """创建一个空的队列"""
    def __init__(self):
        self._queue = []

    def enqueue(self, item):
        """往队列中添加一个item元素"""
        self._queue.append(item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        return self._queue.pop(0)

    def is_empty(self):
        """判断一个队列是否为空"""
        return not self._queue

    def size(self):
        """返回队列的大小"""
        return len(self._queue)


if __name__ == "__main__":
    stack = Queue()
    stack.enqueue(1)
    stack.enqueue(2)
    stack.enqueue(3)
    print(stack.dequeue())
    print(stack.dequeue())
    print(stack.size())