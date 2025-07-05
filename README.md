This is a simple CRUD application based on Python with MySQL database.
This application uses the following:
1. Importing "mysql.connector" connector for using MySQL functions.
2. Concept of user-defined functions for modularising the main objectives of the application:
   i. Creating record
   ii. Reading records
   iii. Updating a record
   iv. Deleting a record
   v. Searching for a record.
3. A menu-driven approach for allowing user to choose what operation he/she wants to perform.
4. Concept of "distinction" between "query" and its "parameters".
5. Concepts of "cursor" and "commiting" transactions after every write (insert/delete/update) operations and its need.

For this project my approach was:
1. Download and install Python IDLE.
2. Download and install pip for command line interface.
3. Download Python Mysql connector using pip. Command: "pip install mysql-connector-python".
4. Check if mysql connector is installed successfully. Open IDLE and in script mode enter: "import mysql.connector". Check for any errors. If no error, it means, the connector is ready for use.
