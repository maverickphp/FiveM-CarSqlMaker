#VERSION 4

import os

# Find multiple .ytd files in a folder
folder_path = 'E:/esx-legacy1.8/server-data/resources/[assets]/[cars]/[car_packs]/mvx_carpack1/stream'
num_files = 100  # Change this to the desired number of files
ytd_files = []

for file_name in os.listdir(folder_path):
    if file_name.endswith('.ytd') and '+hi' not in file_name:
        ytd_files.append(file_name[:-4])  # Remove '.ytd' extension
        if len(ytd_files) == num_files:
            break

if not ytd_files:
    print(f'No .ytd files found in folder or less than {num_files} .ytd files found (excluding files with +h1 in their names)')
    exit()

# Add the file names to a SQL query
query = 'INSERT INTO `importedvehicles` (`name`, `model`, `price`, `category`) VALUES '
values = ', '.join([f"('Mustang302','{file_name}', 1000000, 'ford')" for file_name in ytd_files])

with open('file.sql', 'a') as sql_file:
    sql_file.write(f'{query}{values};\n')

print(f'Added {len(ytd_files)} .ytd files to SQL query (excluding files with +h1 in their names)')