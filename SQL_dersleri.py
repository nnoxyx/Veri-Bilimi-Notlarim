import mysql.connector 
import pandas as pd


"""
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql123",
    database = 'schooldb'
)


# mycursor = mydb.cursor()



# mycursor.execute('CREATE DATABASE mydatabase')
# mycursor.execute('SHOW DATABASES')

# for x in mycursor:
#    print(x)

# mycursor.execute('CREATE TABLE customers (name  VARCHAR(255), address VARCHAR(255))')

print(mydb)

"""

# Insert - kayıt ekleme

"""
def insertProduct(name,price,imageUrl,description ):
    connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql123",
    database = 'not-app'
    )

    cursor = connection.cursor()

    sql = 'INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)'
    values = (name,price,imageUrl,description)

    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f'son eklenen kayıt:{cursor.lastrowid}')

    except mysql.connector.Error as err:
        print('hata:', err)

    finally:
        connection.close()
        print('database bağlantısı kapatıldı')

def insertProducts(list):
    connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql123",
    database = 'not-app'
    )

    cursor = connection.cursor()

    sql = 'INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)'
    values = list

    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f'son eklenen kayıt:{cursor.lastrowid}')

    except mysql.connector.Error as err:
        print('hata:', err)

    finally:
        connection.close()
        print('database bağlantısı kapatıldı')


liste = []
while True:
    name = input('ürün adını girin: ')
    price = float(input('ürün fiyatı: '))
    imageUrl = input('ürün resim adı: ')
    description = input('ürün açıklaması:  ')

    liste.append((name, price, imageUrl, description))

    Result = input('devam etmek istiyor musunuz? (e/h)')
    if Result=='h':
        print('kayıtlarınız veri tabanına aktarılıyor')
        print(liste)
        insertProducts(liste)
        break
# insertProduct(name,price,imageUrl,description)

"""
"""
def InsertMembers(list):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "mysql123",
        database = 'schooldb'
    )

    cursor = connection.cursor()

    sql = 'INSERT INTO new_table(StudentNumber,Name,Surname,BirthDay,Gender) VALUES(%s,%s,%s,%s,%s)'
    values = list
    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f'veriler database e aktarıldı. Son kayıt: {cursor.lastrowid}')

    except mysql.connector.Error as err:
        print('hata:',err)
    
    finally:
        connection.close()
        print('database bağlantısı kapatıldı')
"""
"""
liste1 = []

while True:
    StudentNumber = input('öğrenci numarası:')
    Name = input('öğrenci ismi:')
    Surname = input('öğrenci soyadi:')
    Gender = input('öğrenci cinsiyeti:')



    liste1.append(StudentNumber,Name,Surname,Gender)
    
    result = input('yeni kayıt eklenilecekmi(e/h):')
    if result=='h':
        print('veriler database e aktarıyor')
        print('aktarılan veriler')
        print('\n'.join(liste1))
        InsertMembers(liste1)
        break

"""
import datetime 
"""
list_students = [
    ('101', 'Ali',     'Yılmaz', datetime.datetime(2005, 5, 17), 'E'),
    ('102', 'Canan',   'Can',    datetime.datetime(2005, 6, 17), 'K'),
    ('103', 'Ayşe',    'Tan',    datetime.datetime(2005, 7, 7),  'K'),
    ('104', 'Bahadır', 'Taner',  datetime.datetime(2005, 9, 23), 'E'),
    ('105', 'Ali',     'Toksöz', datetime.datetime(2004, 7, 27), 'E'),
    ('106', 'Cenk',    'Cenk',   datetime.datetime(2003, 8, 25), 'E')
]

InsertMembers(list_students)
print('veriler database e aktarıyor')
print('aktarılan veriler',list_studentsmy)

"""


def insertProduct(name,price,imageUrl,description ):
    connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql123",
    database = 'not-app'
    )

    cursor = connection.cursor()

    sql = 'INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)'
    values = (name,price,imageUrl,description)

    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f'son eklenen kayıt:{cursor.lastrowid}')

    except mysql.connector.Error as err:
        print('hata:', err)

    finally:
        connection.close()
        print('database bağlantısı kapatıldı')

def insertProducts(list):
    connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql123",
    database = 'not-app'
    )

    cursor = connection.cursor()

    sql = 'INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)'
    values = list

    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f'son eklenen kayıt:{cursor.lastrowid}')

    except mysql.connector.Error as err:
        print('hata:', err)

    finally:
        connection.close()
        print('database bağlantısı kapatıldı')


def getProducts():
    connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql123",
    database = 'not-app'
    )

    cursor = connection.cursor()

    #cursor.execute('select * from products')

    #cursor.execute('select * from products where name = "Samsung"')
    cursor.execute('select * from products where name = "Samsung S7" price > 3500')
    cursor.execute('select * from products where name LIKE "%Samsung%"')
    #cursor.execute('select * from products where name LIKE "Samsung%"')
    #cursor.execute('select * from products where name LIKE "%Samsung"')

    #result = cursor.fetchone()
    #print(f'id: {result[0]} name: {result[1]} price: {result[2]}')
    result = cursor.fetchall()

 


    #for product in result: 

    #    print(f'id: {product[0]} name: {product[1]} price: {product[2]}')
    
    
    # df = pd.DataFrame(result)

    # print(df)
    
    #for product in result:
        #print(f'name: {product[1]} price: {product[2]}')
        #print(f'name: {product[0]} price: {product[1]}')


"""
def getProductById(id):
    connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql123",
    database = 'not-app'
    )

  
    cursor = connection.cursor()
    

    sql = 'select * from products where id=%s'
    params = (id,)


    cursor.execute(sql,params)

    result = cursor.fetchone()
    
    print(f'id: {result[0]} name: {result[1]} price: {result[2]}')
    cursor.close()
getProductById(1)
"""

def getProducts():
    connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql123",
    database = 'not-app'
    )

  
    cursor = connection.cursor()
    



    #cursor.execute("select * from products Order By price")
    cursor.execute("select * from products Order By id DESC")

    result = cursor.fetchall()
    
    for product in result:
        print(f'id: {product[0]} name: {product[1]} price: {product[2]}')
    cursor.close()

getProducts()