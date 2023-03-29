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
        #     create_table_query = "CREATE TABLE `get_out`  (id int AUTO_INCREMENT, get_out datetime(6), PRIMARY KEY(id));"
        #                          # "surname varchar(32), " \
        #                          # "get_in datetime(6), " \
        #                          # "get_out datetime(6) , " \
        #                          # "PRIMARY KEY(id));"
        #     cursor.execute(create_table_query)
        #     print("Table created successfully...")

        # INSERT DATA
        with connection.cursor() as cursor:
            insert_query = "INSERT INTO `users`  (name, surname, profession) VALUES ('fkmfyum', 'fymfyumfyum', 'Talyp');"
            cursor.execute(insert_query)
            connection.commit()

        # drop table
        # with connection.cursor() as cursor:
        #     drop_table_query = "DROP TABLE `get_in`;"
        #     cursor.execute(drop_table_query)

        # Select all data from teble
        # with connection.cursor() as cursor:
        #     # select_all_rows = "SELECT * FROM `users`"
        #     cursor.execute("SELECT * FROM `users`")
        #     rows = cursor.fetchall()
        #     for row in rows:
        #         print(row)
        #     print('#' * 20)

        # with connection.cursor() as cursor:
        #     cursor.execute("UPDATE `users` SET  id = '2' WHERE name = 'Azamat';")
    finally:
        connection.close()
except Exception as ex:
    print("connection refused...")
    print(ex)