# Q3. Column Sorting, yay!
# Given a list of dicts, write a program to sort the list according to a key given in input.
# E.g.
# Input f([
# {"fruit": "orange", "color": "orange"},
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"},
# {"fruit": "blueberry", "color": "blue"}
# ], "fruit")
# Should Output
# [
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"},
# {"fruit": "blueberry", "color": "blue"},
# {"fruit": "orange", "color": "orange"}
# ]
# AND
# Input f([
# {"fruit": "orange", "color": "orange"},
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"},
# {"fruit": "blueberry", "color": "blue"}
# ], "color")
# Should Output
# [
# {"fruit": "blueberry", "color": "blue"},
# {"fruit": "orange", "color": "orange"},
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"}
# ]


def sort_list_of_dicts(list_of_dicts, sort_key):
    sorted_list = sorted(list_of_dicts, key=lambda x: x.get(sort_key))
    return sorted_list


# Example usage
data = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

# Sort the list of dicts by fruit
sorted_data = sort_list_of_dicts(data, "fruit")
print("Sorted list of dicts by fruit:")
for item in sorted_data:
    print(item)

# Sort the list of dicts by color
sorted_data = sort_list_of_dicts(data, "color")
print("Sorted list of dicts by color:")
for item in sorted_data:
    print(item)
