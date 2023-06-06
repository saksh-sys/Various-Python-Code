# Q2. Dictionary, what?
# Write a program that returns the file type from a file name. The type of the file is determined
# from the extension. Initially, a list of values of the form "extension,type"(e.g. xls,spreadsheet;
# png,image) will be input.
# The program takes input in the following form:
# 1. Input extension and type values in the form of a string having the following format:
# a. "extension1,type1;extension2,type2;extension3,type3"
# b. E.g. If we needed to input xls → spreadsheet, xlsx → spreadsheet, jpg → image
# our string would be something like: "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
# 2. Input a list of filename.extension. E.g. an input list could be something like ["abc.html",
# "xyz.xls", "text.csv", "123"]
# The program should return a dict of filename: type pairs
# E.g.
# f("xls,spreadsheet;xlsx,spreadsheet;jpg,image", ["abc.jpg",
# "xyz.xls", "text.csv", "123"]) should return
# {
# "abc.jpg": "image",
# "xyz.xls": "spreadsheet",
# "Text.csv": "unknown",
# "123": "unknown"
# }


def get_file_types(extension_type_string, filenames):
    # Parse the extension and type string to create a dictionary
    extension_type_dict = {}
    extensions_types = extension_type_string.split(';')
    for ext_type in extensions_types:
        ext, file_type = ext_type.split(',')
        extension_type_dict[ext] = file_type

    # Create a dictionary of filename: type pairs
    file_types_dict = {}
    for filename in filenames:
        extension = filename.split('.')[-1]  # Extract the extension
        file_type = extension_type_dict.get(extension, 'Unknown')  # Lookup the type in the dictionary
        file_types_dict[filename] = file_type

    return file_types_dict


# Take input from the user
extension_type_string = input("Enter the extension and type values: ")
filenames = input("Enter a list of filenames: ").split(",")  # Split the input string into a list of filenames

# Get the file types dictionary
file_types = get_file_types(extension_type_string, filenames)
print("File types:", file_types)
