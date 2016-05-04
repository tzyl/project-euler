import random


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self.put2(self.root, key, value)

    def put2(self, current_node, key, value):
        if current_node is None:
            return Node(key, value)
        elif key < current_node.key:
            current_node.left = self.put2(current_node.left, key, value)
        elif key > current_node.key:
            current_node.right = self.put2(current_node.right, key, value)
        else:
            current_node.value = value

        current_node.size += 1
        return current_node

    def get(self, key):
        "Returns the value at the node with specified key, None if not there."
        current = self.root
        while current is not None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.value
        return None

    def draw(self):
        current = [self.root]
        while current:
            print [(node.value, node.size) for node in current]
            children = []
            for node in current:
                if node.left is not None:
                    children.append(node.left)
                if node.right is not None:
                    children.append(node.right)
            current = children


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.size = 0
        self.left = None
        self.right = None


bst = BinarySearchTree()
nodes = [(random.randint(0, 100),)*2 for x in xrange(10)]
for node in nodes:
    bst.put(node[0], node[1])

bst.draw()
