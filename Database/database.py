import sqlite3
def func1(a,b):
    c=a+b
    return c

class DataBase():
    def __init__(self,db_name):
        self.conn=sqlite3.connect(db_name)
        self.cursor=self.conn.cursor()

    def CreateTableProducts(self):
        sql_code = (
            'CREATE TABLE IF NOT EXISTS products ('
            'id integer primary key ,'
            'name text,'
            'price integer'
            ');'
        )
        self.cursor.execute(sql_code)

    def CreateTableCatalogs(self):
        sql_code = (('CREATE TABLE IF NOT EXISTS catalogs('
                     'id integer primary key ,'
                     'product_id integer,'
                     'FOREIGN KEY (product_id) REFERENCES products(id)'  #
                     ')'))
        self.cursor.execute(sql_code)
    def CreateAllTables(self):
        self.CreateTableProducts()
        self.CreateTableCatalogs()
    def InsertIntoProducts(self, name: str, price: float):
        sql_code = (('INSERT INTO products (name,price) '
                     'VALUES (?,?);'))
        self.cursor.execute(sql_code, (name, price))






















