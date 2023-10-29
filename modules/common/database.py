import sqlite3
import time

class Database():
    def __init__(self):
        self.connection=sqlite3.connect(r'C:\QA' + r'\become_qa_auto.db')
        self.cursor=self.connection.cursor()
    
    def test_connection(self):
        sqlite_select_query='SELECT sqlite_version();'
        self.cursor.execute(sqlite_select_query)
        record=self.cursor.fetchall()
        print(f'Connection successfully.SQLite Database Version is:{record}')
   
    def get_all_users(self):
        query='SELECT name, address, city FROM customers'
        self.cursor.execute(query)
        record=self.cursor.fetchall()
        return record
    
    def get_user_address_by_name(self,name):
        query=f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record=self.cursor.fetchall()
        return record
    
    def update_product_qnt_by_id(self,product_id,qnt):
        query=f"UPDATE products SET quantity = {qnt} WHERE id={product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self,product_id):
        query=f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self,product_id,name,description,qnt):
        query = f"INSERT OR REPLACE INTO products(id,name,description,quantity)\
            VALUES ({product_id},'{name}','{description}',{qnt})"
        self.cursor.execute(query)
        self.connection.commit()
    
    def delete_product_by_id(self,product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()
    
    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name,\
                products.description, orders.order_date\
                FROM orders\
                JOIN customers ON orders.customer_id = customers.id\
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
        
    def get_table_count(self):
        query = "SELECT name FROM sqlite_master WHERE type='table';" 
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        table_count = [record[0] for record in record]
        return table_count

    def execution_time_of_the_query(self):
        query = "SELECT * FROM customers"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        start_time = time.time()
        end_time = time.time()
        return (start_time, end_time)

    def new_column(self, column_name, table_name):
        query = f"ALTER TABLE {table_name}\
        ADD COLUMN {column_name} TEXT;"
        self.cursor.execute(query)
        self.connection.commit()

    def correctness_of_the_data_type(self):
        query = f"INSERT INTO customer (name) VALUES ('{name}')"
        self.cursor.execute(query)
        self.connection.commit()
    
    def select_customer_data(self, customer_name):
        query = f"SELECT id, address, city, postalCode, country FROM customers WHERE name = '{customer_name}'"
        self.cursor.execute(query)
        data = self.cursor.fetchone()
        return data

    def modify_customer_data(self, customer_id, new_address, new_city, new_postal_code, new_country):
        query = f"""
        UPDATE customers
        SET address = '{new_address}', city = '{new_city}',
            postalCode = '{new_postal_code}', country = '{new_country}'
        WHERE id = {customer_id}
    """
        self.cursor.execute(query)
        self.connection.commit()

    def delete_customer(self, customer_name):
        query = f"DELETE FROM customers WHERE name = '{customer_name}'"
        self.cursor.execute(query)
        self.connection.commit()

    def customer_exists(self, customer_name):
        query = f"SELECT COUNT(*) FROM customers WHERE name = '{customer_name}'"
        self.cursor.execute(query)
        count = self.cursor.fetchone()[0]
        return count > 0