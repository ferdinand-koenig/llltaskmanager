import unittest
import numpy as np
from lll_taskmanager import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        """Set up the TaskManager instance and test data."""
        self.task_manager = TaskManager()
        # Generate test data
        self.X1_1 = np.random.normal(loc=0, scale=1, size=(100, 10))
        self.X1_2 = np.random.normal(loc=0, scale=1, size=(100, 10))
        self.X1_3 = np.random.normal(loc=0, scale=1, size=(70, 10))
        self.X2_1 = np.random.normal(loc=5, scale=1, size=(100, 10))
        self.X2_2 = np.random.normal(loc=5, scale=1, size=(100, 10))
        self.X3_1 = np.random.uniform(low=-5, high=5, size=(100, 10))
        self.X3_2 = np.random.uniform(low=-5, high=5, size=(100, 10))
        self.X3_3 = np.random.uniform(low=-5, high=5, size=(80, 10))

        # X1_1 = np.random.normal(loc=0, scale=1, size=(100, 10))
        # X1_2 = np.random.normal(loc=0, scale=1, size=(100, 10))
        # X1_3 = np.random.normal(loc=0, scale=1, size=(70, 10))
        # X2_1 = np.random.normal(loc=5, scale=1, size=(100, 10))
        # X2_2 = np.random.normal(loc=5, scale=1, size=(100, 10))
        # X3_1 = np.random.uniform(low=-5, high=5, size=(100, 10))
        # X3_2 = np.random.uniform(low=-5, high=5, size=(80, 10))

        self.task_counter = -1

    def test_add_task(self):
        """Test adding a new task."""
        result = self.task_manager.detect(self.X1_1)  # Detect task
        self.task_counter += 1
        print(f"Return for X1_1: {result}.")
        self.assertTrue(result[0], "X1 should match an existing task (itself).")

    def test_detect_new_task(self):
        """Test detecting a new task."""
        result = self.task_manager.detect(self.X2_1)  # Detect X2 as a new task
        self.task_counter += 1
        print(f"Return for X2_1: {result}.")
        self.assertTrue(result[0], "X2 should be detected as a new task.")

    def test_detect_task1(self):
        """Test detecting a new task."""
        result = self.task_manager.detect(self.X1_2)
        print(f"Return for X1_2: {result}.")
        self.assertFalse(result[0], "X1_2 should match an existing task.")
        self.assertEqual(result[1], 0, "X1_2 should have been assigned to the first task")
        result = self.task_manager.detect(self.X1_3)  # Detect X1_3
        print(f"Return for X1_3: {result}.")
        self.assertFalse(result[0], "X1_3 should match an existing task.")
        self.assertEqual(result[1], 0, "X1_3 should have been assigned to the first task.")

    def test_detect_task2(self):
        result = self.task_manager.detect(self.X2_2)
        print(f"Return for X2_1: {result}.")
        self.assertEqual(result[1], self.task_counter, "X2_2 should have been assigned to the second task.")

    def test_detect_task3(self):
        result = self.task_manager.detect(self.X3_1)
        print(f"Return for X3_1: {result}.")
        self.assertFalse(result[0], "X3_1 should be assigned a new task.")
        self.task_counter += 1

        result = self.task_manager.detect(self.X3_2)
        print(f"Return for X3_2: {result}.")
        self.assertEqual(result[1], self.task_counter, "X3_2 should be assigned to the third task.")

    def test_delete_task(self):
        self.task_manager.delete_task(0)

        result = self.task_manager.detect(self.X1_2)
        self.task_counter += 1
        print(f"Return for X1_2 after deleting first task: {result}.")
        self.assertTrue(result[0], "X1_2 should not match an existing task.")
        self.assertEqual(result[1], self.task_counter, "X1_2 should have been assigned to a new task id.")

        result = self.task_manager.detect(self.X1_1)
        print(f"Return for X1_1: {result}.")
        self.assertEqual(result[0], self.task_counter, f"X1_1 should match task {self.task_counter}.")


if __name__ == "__main__":
    unittest.main()
