def lists_to_dict(keys, values):
    # Check if the lengths of the lists are equal
    if len(keys) != len(values):
        raise ValueError("Lengths of keys and values lists must be equal")

    # Create a dictionary using zip() function
    result_dict = dict(zip(keys, values))
    
    return result_dict

K = [1001, 1002, 1003, 1004, 1005]
V = ["USA", "Canada", "China", "Japan", "UK"]

result_dict = lists_to_dict(K, V)
print(result_dict)
