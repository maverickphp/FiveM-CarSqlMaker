import os

def get_user_input():
    category = input("Enter the category name: ")
    while True:
        try:
            price = int(input("Enter the price: "))
            break
        except ValueError:
            print("Please enter a valid integer for the price.")
    return category, price

def find_ytd_files(folder_path, num_files):
    ytd_files = []
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if (file_name.endswith('.ytd') and 
                '+hi' not in file_name and 
                '-' not in file_name and 
                '_' not in file_name):
                ytd_files.append(file_name[:-4])  # Remove '.ytd' extension
                if len(ytd_files) == num_files:
                    return ytd_files
    return ytd_files

def main():
    folder_path = input("Enter the folder path: ")
    num_files = int(input("Enter the desired number of files: "))
    
    category, price = get_user_input()
    
    ytd_files = find_ytd_files(folder_path, num_files)

    if not ytd_files:
        print(f'No .ytd files found in folder or less than {num_files} .ytd files found (excluding files with +hi, -, or _ in their names)')
        return

    # Add the file names to a SQL query
    query = 'INSERT INTO `importedvehicles` (`name`, `model`, `price`, `category`) VALUES '
    values = ',\n'.join([f"('{file_name}','{file_name}', {price}, '{category}')" for file_name in ytd_files])

    sql_filename = 'importedvehicles.sql'
    file_exists = os.path.isfile(sql_filename)

    with open(sql_filename, 'a') as sql_file:
        if not file_exists:
            sql_file.write("-- Create table if not exists\n")
            sql_file.write("CREATE TABLE IF NOT EXISTS `importedvehicles` (\n")
            sql_file.write("  `name` varchar(255) NOT NULL,\n")
            sql_file.write("  `model` varchar(255) NOT NULL,\n")
            sql_file.write("  `price` int(11) NOT NULL,\n")
            sql_file.write("  `category` varchar(255) NOT NULL\n")
            sql_file.write(") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;\n\n")

        sql_file.write(f'{query}\n{values};\n\n')  # Each query on a new line

    print(f'Added {len(ytd_files)} .ytd files to SQL query in {sql_filename} (excluding files with +hi, -, or _ in their names)')

if __name__ == "__main__":
    main()