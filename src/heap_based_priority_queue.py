class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class BinaryHeap(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def node_up(self):
        i = len(self) - 1
        while i > 0:
            parent_index = (i - 1) // 2
            if self.items[i].priority < self.items[parent_index].priority:
                self.items[i], self.items[parent_index] = self.items[parent_index], self.items[i]
                i = parent_index
            else:
                break

    def insert(self, value, priority):
        node = Node(value, priority)
        self.items.append(node)
        self.node_up()

    def node_down(self, i):
        while 2 * i + 1 < len(self):
            mc = self.min_child(i)+
            if self.items[i].priority > self.items[mc].priority:
                self.items[i], self.items[mc] = self.items[mc], self.items[i]
            i = mc

    def min_child(self, i):
        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2

        if right_child_index >= len(self.items):
            return left_child_index
        else:
            if self.items[left_child_index].priority < self.items[right_child_index].priority:
                return left_child_index
            else:
                return right_child_index

    def delete_min(self):
        if len(self.items) == 0:
            return None
        elif len(self.items) == 1:
            return self.items.pop()
        else:
            return_value = self.items[0]
            self.items[0] = self.items.pop()
            self.node_down(0)
            return return_value

    def build_heap(self, alist):
        self.items = alist
        i = len(alist) // 2 - 1
        while i >= 0:
            self.node_down(i)
            i = i - 1
