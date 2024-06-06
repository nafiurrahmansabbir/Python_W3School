def create_array(size):
    try:
        # Create an array with `size` elements, initialized to zero
        array = [0] * size
        print(f"Array created with {size} elements.")
        
        # Attempt to access an out-of-bound element to raise an IndexError
        out_of_bound_index = size  # This index is out of bounds (0-based index)
        print(f"Accessing element at index {out_of_bound_index}: {array[out_of_bound_index]}")
    
    except IndexError as e:
        print(f"Exception caught: {e}")

if __name__ == "__main__":
    S = int(input("Enter the number of elements for the array: "))
    create_array(S)
