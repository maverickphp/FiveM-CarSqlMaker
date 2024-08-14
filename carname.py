import os

# Find multiple .ytd files in a folder and its subfolders
folder_path = 'C:/Users/fasih/Downloads/100carpack/5ive'
num_files = 150  # Change this to the desired number of files
ytd_files = []

# Traverse the directory tree
for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith('.ytd') and '+hi' not in file_name:
            ytd_files.append(file_name[:-4])  # Remove '.ytd' extension
            if len(ytd_files) == num_files:
                break
    if len(ytd_files) == num_files:
        break

if not ytd_files:
    print(f'No .ytd files found in folder or less than {num_files} .ytd files found (excluding files with +h1 in their names)')
    exit()

# Add the file names to a SQL query
query = 'INSERT INTO `importedvehicles` (`name`, `model`, `price`, `category`) VALUES '
values = ', '.join([f"('{file_name}','{file_name}', 1000000, 'CarCategory')" for file_name in ytd_files])

with open('file.sql', 'a') as sql_file:
    sql_file.write(f'{query}{values};\n')

print(f'Added {len(ytd_files)} .ytd files to SQL query (excluding files with +h1 in their names)')
