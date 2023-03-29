
import pymysql
from config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host= host,
        port= 3306,
        user= user,
        password= password,
        database= db_name,
        cursorclass= pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)


    try:
        # CREATE TABLE
        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `users`  (id int AUTO_INCREMENT, " \
        #                          "name varchar(32), " \
        #                          "password varchar(32), " \
        #                          "email varchar(32), PRIMARY KEY(id));"
        #     cursor.execute(create_table_query)
        #     print("Table created successfully...")

        # INSERT DATA
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users`  (name, password, email) VALUES ('Anna', 'qwerty', 'anna@gmail.com');"
        #     cursor.execute(insert_query)
        #     connection.commit()

        # Select all data from teble
        with connection.cursor() as cursor:
            # select_all_rows = "SELECT * FROM `users`"
            cursor.execute("SELECT * FROM `users`")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print('#' * 20)
    finally:
        connection.close()
except Exception as ex:
    print("connection refused...")
    print(ex)