class Node:
    def __init__(self, key, val):
        # Store key + value
        # WHY key? → needed to delete from hashmap during eviction
        self.key, self.val = key, val

        # Pointers for doubly linked list
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity

        # HashMap: key → node
        # WHY? → O(1) access to nodes
        self.cache = {}

        # Create dummy nodes for left (LRU) and right (MRU)
        # WHY dummy nodes? → simplify insert/remove logic (no edge cases)
        self.left = Node(0, 0)   # Least Recently Used
        self.right = Node(0, 0)  # Most Recently Used

        # Connect dummy nodes
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        # Remove node from linked list
        # WHY? → needed when updating or evicting nodes
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        # Insert node at the right (most recently used position)
        # WHY right side? → we treat right as MRU end
        prev, nxt = self.right.prev, self.right

        # Insert node between prev and right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt


    def get(self, key: int) -> int:
        if key in self.cache:
            # Move accessed node to MRU position
            # WHY? → recently used items should not be evicted
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val

        # Key not found
        return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old node if key already exists
            # WHY? → we will insert updated node at MRU position
            self.remove(self.cache[key])

        # Insert new node into hashmap
        self.cache[key] = Node(key, value)

        # Insert into linked list as MRU
        self.insert(self.cache[key])

        # If capacity exceeded → remove LRU node
        if len(self.cache) > self.cap:
            # LRU node is next to left dummy
            lru = self.left.next

            # Remove from linked list
            self.remove(lru)

            # Delete from hashmap
            # WHY? → keep both structures in sync
            del self.cache[lru.key]