from multiprocessing import connection
import mysql.connector


# 建立連線
connection = mysql.connector.connect(host="localhost",
                                    port = "3306",
                                    user ="root",
                                    password = "respect412")

# 把剛剛建立的連線寫入 cousor 裡面
cursor = connection.cursor()

# 創建資料庫
# cursor.execute("CREATE DATABASE `qq`;")

# 取得所有資料庫名稱
# cursor.execute("SHOW DATABASES;")
# records = cursor.fetchall()
# for  r in records:
#     print(r)

# 使用資料庫
# cursor.execute("USE `sql_tutorial`;")

# 創建表格
cursor.execute("CREATE TABLE `student`(`student_id` INT,`name` VARCHAR(20),`major` VARCHAR(20),PRIMARY KEY(`student_id`));")

# cursor.execute("SELECT * FROM `qq`;")

#關閉 cursor ＆ 關閉連線
cursor.close()
connection.close()
