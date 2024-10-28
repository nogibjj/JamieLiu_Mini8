import unittest
import random
import time
import tracemalloc
from main import merge_sort


class TestMergeSort(unittest.TestCase):
    def benchmark_merge_sort(self, array_size):
        """
        Helper function to benchmark merge_sort with a random list of a given size.

        Parameters:
        array_size (int): The size of the array to sort.

        Returns:
        tuple: (float, int) - The time taken in seconds and peak memory usage in bytes.
        """
        test_data = random.sample(range(array_size * 2), array_size)

        tracemalloc.start()
        start_time = time.time()
        merge_sort(test_data)
        end_time = time.time()
        current, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        time_taken = end_time - start_time  # Time in seconds
        return time_taken, peak_memory

    def test_performance(self):
        """
        Benchmark merge_sort with various input sizes and print the results.
        """
        sizes = [100, 1_000, 10_000, 100_000, 1_000_000]
        with open("python_merge_sort_benchmark.csv", "w") as f:
            f.write("Size,Time (s),Memory (bytes)\n")
            for size in sizes:
                time_taken, peak_memory = self.benchmark_merge_sort(size)
                f.write(f"{size},{time_taken:.6f},{peak_memory}\n")
                print(f"{size},{time_taken:.6f},{peak_memory}")


if __name__ == "__main__":
    unittest.main()
