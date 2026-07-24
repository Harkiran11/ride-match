class _Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self._root = None
        self._count = 0

    def __len__(self):
        return self._count

    def insert(self, key, value):
        self._count += 1
        if self._root is None:
            self._root = _Node(key, value)
            return
        node = self._root
        while True:
            if key < node.key:
                if node.left is None:
                    node.left = _Node(key, value)
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = _Node(key, value)
                    return
                node = node.right

    def search(self, key):
        node = self._root
        while node is not None:
            if key == node.key:
                return node.value
            node = node.left if key < node.key else node.right
        return None

    def in_order(self):
        result = []

        def visit(node):
            if node is None:
                return
            visit(node.left)
            result.append((node.key, node.value))
            visit(node.right)

        visit(self._root)
        return result

    def range_query(self, low, high):
        result = []

        def visit(node):
            if node is None:
                return
            if node.key > low:
                visit(node.left)
            if low <= node.key <= high:
                result.append((node.key, node.value))
            if node.key < high:
                visit(node.right)

        visit(self._root)
        return result

    def height(self):
        def visit(node):
            if node is None:
                return 0
            return 1 + max(visit(node.left), visit(node.right))

        return visit(self._root)
