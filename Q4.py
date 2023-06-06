# Q4. The power of one line -
# Given a dictionary, switch position of key and values in the dict, i.e., value becomes the key and
# key becomes value. The function's body shouldn't have more than one statement.
# f({
# "key1": "value1",
# "key2": "value2",
# "key3": "value3",
# "key4": "value4",
# "key5": "value5"
# }) should return
# {
# "value1": "key1",
# "value2": "key2",
# "value3": "key3",
# "value4": "key4",
# "value5": "key5"
# }


def switch_key_value(dictionary):
    return {v: k for k, v in dictionary.items()}
input_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

switched_dict = switch_key_value(input_dict)
print(switched_dict)
