# FiveM-CarSqlQueryMaker

<h3>YTD File Uploader</h3>
This Python program uploads a file .ytd, copies multiple names, and adds them to a SQL file. It finds the names with the .ytd format from the folder and removes the .ytd extension when writing the names to the SQL query. It also excludes any names that contain +h1 in them and formats the code to make it more readable.

<h4>Requirements</h4>
- Python 3.x

<h4>How to use</h4>

1. Clone the code to your system
2. Edit the carname.py file
3. On line no 6, you can change the directory of carpack stream folder
4. On line no 7, you can change the number of queries you want to write
6. Save and close the file
7. Open the .start file and your query will be written in the file.sql file

<b><h3>NOTE:</h3></b>
If you have any issue you can open a thread in issues.
Thanks!


pyinstaller --onefile --clean carname.py
