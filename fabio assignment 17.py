def find_common_elements(list1, list2):
    common = []
    for item in list1:
        if item in list2:
            common.append(item)
    return common


# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

result = find_common_elements(list1, list2)
print("Common elements:", result)