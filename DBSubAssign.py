import sqlite3


# Function to create a database and a table 
def create_database():
    conn = sqlite3.connect('files.db')

    with conn :
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fName VARCHAR(255) \
            )")
        conn.commit()
    conn.close()


# Function to insert file names into the database  
def insert_file_names(fileList):
    conn = sqlite3.connect('files.db')

    with conn :
        cur = conn.cursor()

        for filename in fileList:
            if filename.endswith('.txt'):
                cur.execute("INSERT INTO tbl_files (col_fName) VALUES (?)", (filename,)) 
        conn.commit()
    conn.close()
            

# Function to retrieve and print all '.txt' file names from the database  
def print_files():
    conn = sqlite3.connect('files.db')

    with conn :
        cur = conn.cursor()
        cur.execute("SELECT col_fname FROM tbl_files")
        varFilename = cur.fetchall()
        for item in varFilename:
            msg = "File Name: {}".format(item[0])
            print(msg)
    conn.close()


if __name__ == "__main__":
    fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
    
    # Create the database and table
    create_database()

    # Insert the file names that end with '.txt' file names into the database
    insert_file_names(fileList)

    # Print the qualifying '.txt' file names from the database
    print_files()





        
