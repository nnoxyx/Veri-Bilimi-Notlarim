import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql123",
    database = 'schooldb'
)

cursor = connection.cursor()

# Tablodaki sütunu düzelten SQL komutunu çalıştırıyoruz
cursor.execute("ALTER TABLE new_table MODIFY BirthDay DATETIME;")

print("Sütun tipi başarıyla düzeltildi! Artık ana kodunu çalıştırabilirsin.")

cursor.close()
connection.close()