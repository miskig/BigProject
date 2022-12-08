import sys
import pyodbc

# Get the file name and text from the command line arguments
file_name = sys.argv[1]
text = sys.argv[2]

# Connect to the SQL Server database
cnxn = pyodbc.connect('Data Source=(localdb)\MSSQLLocalDB;'
                      'Initial Catalog=Syllabi;'
                      'Integrated Security=True;'
                      'Connect Timeout=30;'
                      'Encrypt=False;'
                      'TrustServerCertificate=False;'
                      'ApplicationIntent=ReadWrite;'
                      'MultiSubnetFailover=False')

# Create a cursor to execute queries
cursor = cnxn.cursor()

# Insert the file name and text into the database
query = 'INSERT INTO HS.Plaintext (file_name, file_text) VALUES (SFileName, Plaintext)'
cursor.execute(query, file_name, text)
cnxn.commit()

# Close the cursor and connection
cursor.close()
cnxn.close()
