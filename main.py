
import sqlite3
from Database import database as d
db_name='maxim_db'
db=d.DataBase(db_name)
db.CreateAllTables()


# conn.execute("DROP TABLE if exists products")
# conn.execute("DROP TABLE  if exists catalogs")
# d.CreateTableProducts(cursor)
# d.CreateTableCatalogs(cursor)
# d.InsertIntoProducts(cursor,"Форель",3700)
# insert_into_products_query=('INSERT INTO products (name,price) '
#                             'VALUES (?,?);')
#
# inserting_values1=("Форель",1249)
# inserting_values2=("Дыня",200)
# inserting_values3=("Арбуз",400)
# inserting_values4=("Дыня",415)
# select_from_products_query=('SELECT * FROM products')
# select_for_catalog_query=('SELECT id FROM products  WHERE price>250')
# insert_into_catalog_query=('INSERT INTO catalogs (product_id) VALUES (?);')
#
# cursor.execute(create_catalogs_table_query)
# cursor.execute(insert_into_products_query,inserting_values1)
# cursor.execute(insert_into_products_query,inserting_values2)
# cursor.execute(insert_into_products_query,inserting_values3)
# cursor.execute(insert_into_products_query,inserting_values4)
# #cursor.execute(select_from_products_query)
# #print(cursor.fetchall())
#
# cursor.execute(select_for_catalog_query)
# id=cursor.fetchall()
# for i in id:
#     cursor.execute(insert_into_catalog_query,(i[0],))
# cursor.execute('SELECT name,price FROM catalogs '
#                'join products on catalogs.product_id=products.id')
# print(cursor.fetchall())
# conn.commit()
# conn.close()