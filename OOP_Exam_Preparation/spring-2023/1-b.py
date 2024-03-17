def process_data(data):
    # Sorting the data
    sorted_data = sorted(data)
    
    # Reversing the sorted data
    # reversed_data = sorted_data[::-1]
    sorted_data.reverse()
    
    return sorted_data

# Example usage:
d = [181, 178, 187, 182, 192, 189, 202, 201]
processed_d = process_data(d)
print("Original data:", d)
print(f"Processed data (reverse-sorted): {processed_d}")
