class MemoryManager:
    def __init__(self, blocks):
        """
        Initialize the memory manager with a list of memory blocks.
        :param blocks: List of memory block sizes
        """
        self.blocks = blocks  # List of memory blocks
 
    def worst_fit_allocation(self, processes):
        """
        Allocate memory to processes using the Worst Fit algorithm.
        :param processes: List of process sizes
        :return: List of allocated block indices for each process (-1 if not allocated)
        """
        allocation = [-1] * len(processes)
 
        for i in range(len(processes)):
            # Find the largest block that fits the process
            worst_index = -1
            for j in range(len(self.blocks)):
                if self.blocks[j] >= processes[i]:
                    if worst_index == -1 or self.blocks[j] > self.blocks[worst_index]:
                        worst_index = j
 
            # Allocate memory if a suitable block is found
            if worst_index != -1:
                allocation[i] = worst_index
                self.blocks[worst_index] -= processes[i]
 
        return allocation
 
    def display_status(self):
        """
        Display the current status of memory blocks.
        """
        print("Current memory block sizes:", self.blocks)
 
    @staticmethod
    def validate_input(input_string):
        """
        Validate user input to ensure it's a list of positive integers.
        :param input_string: Input string from the user
        :return: List of integers if valid, otherwise raises ValueError
        """
        try:
            values = list(map(int, input_string.split()))
            if any(value <= 0 for value in values):
                raise ValueError("All values must be positive integers.")
            return values
        except ValueError:
            raise ValueError("Invalid input. Please enter a list of positive integers.")
 
if __name__ == "__main__":
    try:
        # Input memory blocks
        print("Enter the sizes of memory blocks, separated by spaces:")
        blocks = MemoryManager.validate_input(input())
        manager = MemoryManager(blocks)
 
        # Input processes
        print("Enter the sizes of processes, separated by spaces:")
        processes = MemoryManager.validate_input(input())
 
        # Allocate memory
        allocation = manager.worst_fit_allocation(processes)
 
        # Display results
        print("\nProcess No.\tProcess Size\tBlock No.")
        for i in range(len(processes)):
            if allocation[i] != -1:
                print(f"{i + 1}\t\t{processes[i]}\t\t{allocation[i] + 1}")
            else:
                print(f"{i + 1}\t\t{processes[i]}\t\tNot Allocated")
 
        # Display memory block status
        manager.display_status()
 
    except ValueError as e:
        print(e)
 
