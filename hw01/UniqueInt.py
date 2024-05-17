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

class UniqueInt:
    def processFile(self, input_file_path, output_file_path):
        with open(input_file_path, 'r') as input_file:
            # Process the file content here
            pass
        # Write output to output_file_path

    def processFiles(self, input_file_paths, output_file_paths):
        for input_file_path, output_file_path in zip(input_file_paths, output_file_paths):
            self.processFile(input_file_path, output_file_path)

    def processFiles(self, inputFilePaths, outputFilePaths):
       
        unique_integers = []

        # Start measuring time and memory usage
        start_time = time.time()
        tracemalloc.start()

        # Sort unique integers using custom bubble sort
        sorted_unique_integers = self.bubble_sort(unique_integers)

        # Write the sorted unique integers to the output file
        '''with open(outputFilePaths,'w') as output_file:
            for integer in sorted_unique_integers:
                output_file.write(f"{integer}\n")'''


    def processFiles(self, input_file_paths, output_file_paths):
        for input_file_path, output_file_path in zip(input_file_paths, output_file_paths):
            self.processFile(input_file_path, output_file_path)

            # Open the output file for writing
            with open(output_file_path, 'w') as output_file:
                # Write output to the output file
                pass  # You need to implement this part

        # Stop measuring time and memory usage
        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        start_time = time.time()

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
    input_file_paths = [
    "sample_inputs/small_sample_input_01.txt",
    "sample_inputs/small_sample_input_02.txt",
    "sample_inputs/small_sample_input_03.txt",
    "sample_inputs/small_sample_input_04.txt"
    # Add more file paths as needed
]

    output_file_paths= [
            "sample_results/small_sample_results_01.txt",
            "sample_results/small_sample_results_02.txt",
            "sample_results/small_sample_results_03.txt",
            "sample_results/small_sample_results_04.txt",                                                                   
            ]
    unique_int_processor.processFiles(input_file_paths, output_file_paths)

