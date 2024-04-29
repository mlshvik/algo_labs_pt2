import unittest
from src.heap_based_priority_queue import BinaryHeap, Node


class TestBinaryHeap(unittest.TestCase):
    def test_insert_and_delete_min(self):
        binary_heap = BinaryHeap()
        binary_heap.insert('Task 1', 5)
        binary_heap.insert('Task 2', 3)
        binary_heap.insert('Task 3', 7)

        self.assertEqual(binary_heap.delete_min().value, 'Task 2')
        self.assertEqual(binary_heap.delete_min().value, 'Task 1')

    def test_insert_and_delete_min_with_equal_priorities(self):
        binary_heap = BinaryHeap()
        binary_heap.insert('Task 4', 4)
        binary_heap.insert('Task 5', 4)
        binary_heap.insert('Task 6', 4)

        self.assertEqual(binary_heap.delete_min().value, 'Task 4')
        self.assertEqual(binary_heap.delete_min().value, 'Task 6')
        self.assertEqual(binary_heap.delete_min().value, 'Task 5')

    def test_insert_and_delete_min_with_different_priorities(self):
        binary_heap = BinaryHeap()
        binary_heap.insert('Task 7', 1)
        binary_heap.insert('Task 8', 2)
        binary_heap.insert('Task 9', 3)

        self.assertEqual(binary_heap.delete_min().value, 'Task 7')
        self.assertEqual(binary_heap.delete_min().value, 'Task 8')
        self.assertEqual(binary_heap.delete_min().value, 'Task 9')

    def test_build_heap(self):
        binary_heap = BinaryHeap()
        # Створюємо об'єкти класу Node для кожного кортежу переданого списку
        binary_heap.build_heap([Node('Task 10', 2), Node('Task 11', 1), Node('Task 12', 3)])

        # Отримуємо значення через атрибут value об'єкта Node
        self.assertEqual(binary_heap.delete_min().value, 'Task 11')
        self.assertEqual(binary_heap.delete_min().value, 'Task 10')
        self.assertEqual(binary_heap.delete_min().value, 'Task 12')


if __name__ == '__main__':
    unittest.main()
