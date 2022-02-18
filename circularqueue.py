# -*- coding: utf-8 -*-


# Если размер буфера выбран правильно - эффективное использование памяти; Если не критична потеря данных при записи в полный буфер, можно модифицировать.
# Resize - вермя и памяти затаратный.
class FixedCircularBuffer:

    def __init__(self, size):
        self._maxSize = size
        self._firstIndex = 0
        self._lastIndex = 0
        self._curSize = 0
        self._buffer = [None] * size

    @property
    def empty(self):
        return self._curSize == 0

    @property
    def full(self):
        return self._curSize == self._maxSize

    def enqueue(self, elem):
        if self.full:
            return
        self._buffer[self._lastIndex] = elem
        self._lastIndex = (self._lastIndex + 1) % self._maxSize
        self._curSize += 1

    def dequeue(self):
        if self.empty:
            return
        value = self._buffer[self._firstIndex]
        self._firstIndex = (self._firstIndex + 1) % self._maxSize
        self._curSize -= 1
        return value


class Node:

    def __init__(self, elem):
        self._elem = elem
        self._next = None

    @property
    def value(self):
        return self._elem

    @property
    def nextNode(self):
        return self._next

    @nextNode.setter
    def nextNode(self, elem):
        self._next = elem

# Динамическая величина буфера.
# Каждый элемент занимает больше памяти.
class FlexCircularBuffer:

    def __init__(self):
        self._firstNode = None
        self._lastNode = None

    @property
    def empty(self):
        return self._firstNode is None

    def enqueue(self, elem):
        node = Node(elem)
        if self._firstNode is None:
            self._firstNode = node
            self._lastNode = node
        else:
            self._lastNode.nextNode = node
            self._lastNode = node

    def dequeue(self):
        value = self._firstNode.value
        self._firstNode = self._firstNode.nextNode
        return value

