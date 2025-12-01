# Function to sort a list of numbers in ascending order
def sort_list(numbers):
    """
    Takes a list of numbers and returns a new list sorted in ascending order.
    """
    # Using the built-in sorted() function to create a new sorted list
    sorted_numbers = sorted(numbers)
    return sorted_numbers

# Example usage
if __name__ == "__main__":
    # Sample list of numbers
    my_numbers = [34, 7, 23, 32, 5, 62]

    # Call the sort_list function
    sorted_numbers = sort_list(my_numbers)

    # Print the original and sorted lists
    print("Original list:", my_numbers)
    print("Sorted list:", sorted_numbers)