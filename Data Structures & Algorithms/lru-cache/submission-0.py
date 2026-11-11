class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(-1,0)
        self.tail = Node(-1,0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.get(key)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
            if len(self.cache) > self.capacity:
                temp = self.head.next
                self.remove(temp)
                del self.cache[temp.key]


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def insert(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
