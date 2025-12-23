import pymysql

# Step 1: Connect to the database
connection = pymysql.Connect(
    host='localhost',
    user='root',
    password='root',
    database='test', # Make sure this DB exists
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:

        # Step 2: Create a Table
        create_query = """
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            department VARCHAR(100)
        );
        """
        cursor.execute(create_query)

        # Step 3: Insert Data
        insert_query = "INSERT INTO employees (name, department) VALUES (%s, %s)"
        values = [("John", "IT"), ("Alice", "HR"), ("Bob", "Finance")]
        cursor.executemany(insert_query, values)
        connection.commit()

        # Step 4: Select Data
        select_query = "SELECT * FROM employees"
        cursor.execute(select_query)
        result = cursor.fetchall()

        for row in result:
            print(row)

        # Step 5: Write row to file
        with open("employee_output.txt", "w") as f:
            for row in result:
                f.write(f"{row}\n")
finally:
    connection.close()


