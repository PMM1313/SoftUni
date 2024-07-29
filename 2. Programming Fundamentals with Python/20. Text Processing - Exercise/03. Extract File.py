# Read the input file path
file_path = input()

# Split the file path to get the file name with extension
path_parts = file_path.split('\\')
file_with_extension = path_parts[-1]

# Split the file name and extension
file_name, file_extension = file_with_extension.split('.')

# Print the results
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
