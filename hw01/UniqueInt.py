import time
import tracemalloc

class UniqueInt:
    def __init__(self):
        """
        Initializes the UniqueInt object with a boolean array to track seen integers.
        """
        self.seen = [False] * 2047  # Array to track integers from -1023 to 1023

    def readNextItemFromFile(self, inputFileStream):
        """
        Reads the next integer item from the input file stream, skipping invalid lines.

        Args:
        inputFileStream (file object): The input file stream.

        Returns:
        int or None: The next valid integer from the file, or None if end of file is reached.
        """
        while True:
            line = inputFileStream.readline()
            if not line:
                return None
            line = line.strip()
            if line:  # Skip empty lines
                try:
                    integer = int(line)
                    return integer
                except ValueError:
                    continue  # Skip lines that do not contain a valid integer

    def processFile(self, inputFilePath, outputFilePath):
        """
        Processes an input file to extract unique integers, sort them, and write to an output file.

        Args:
        inputFilePath (str): The path to the input file containing integers.
        outputFilePath (str): The path to the output file to write sorted unique integers.
        """
        unique_integers = []

        # Start measuring time and memory usage
        start_time = time.time()
        tracemalloc.start()

        with open(inputFilePath, 'r') as input_file:
            while True:
                integer = self.readNextItemFromFile(input_file)
                if integer is None:
                    break
                if not self.seen[integer + 1023]:
                    self.seen[integer + 1023] = True
                    unique_integers.append(integer)

        # Sort unique integers using custom bubble sort
        sorted_unique_integers = self.bubble_sort(unique_integers)

        # Write the sorted unique integers to the output file
        with open(outputFilePath, 'w') as output_file:
            for integer in sorted_unique_integers:
                output_file.write(f"{integer}\n")

        # Stop measuring time and memory usage
        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # Print the runtime and peak memory usage
        print(f"Runtime: {end_time - start_time:.6f} seconds")
        print(f"Memory usage: {peak / 10**6:.6f} MB")

    def bubble_sort(self, arr):
        """
        Sorts an array of integers in ascending order using the bubble sort algorithm.

        Args:
        arr (list of int): The input list of integers to be sorted.

        Returns:
        list of int: The sorted list of integers.
        """
        r = len(arr)
        for a in range(r):
            for w in range(0, r - a - 1):
                if arr[a] > arr[a + 1]:
                    arr[a], arr[a + 1] = arr[a + 1], arr[a]
        return arr

# Example usage
if __name__ == "__main__":
    unique_int_processor = UniqueInt()
    input_file_path = "Data-structures-Algorithms/hw01/sample_inputs/small_sample_input_01.txt"
    output_file_path = "Data-structures-Algorithms/hw01/sample_results/small_sample_input_01.txt_results.txt"
    unique_int_processor.processFile(input_file_path, output_file_path)

