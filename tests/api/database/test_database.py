import pytest 
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db=Database()
    db.test_connection()

@pytest.mark.database
def test_ceck_all_users():
    db=Database()
    users=db.get_all_users()

    print(users)

@pytest.mark.database
def test_check_user_sergii():
    db=Database()
    user=db.get_user_address_by_name('Sergii')

    assert user[0][0]=='Maydan Nezalezhnosti 1'
    assert user[0][1]=='Kyiv'
    assert user[0][2]=='3127'
    assert user[0][3]=='Ukraine'

@pytest.mark.database
def test_product_qnt_update():
    db= Database()
    db.update_product_qnt_by_id(1,25)
    water_qnt=db.select_product_qnt_by_id(1)

    assert water_qnt[0][0]==25

@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво','солодке',30)
    water_qnt=db.select_product_qnt_by_id(4)

    assert water_qnt[0][0]==30
    
@pytest.mark.database  
def test_product_delete():
    db = Database()
    db.insert_product(99,'тестові','дані',999)
    db.delete_product_by_id(99)
    qnt=db.select_product_qnt_by_id(99)

    assert len(qnt)==0

@pytest.mark.database   
def test_detailed_orders():
    db=Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)

    assert len(orders)==1

    assert orders[0][0]==1
    assert orders[0][1]=='Sergii'
    assert orders[0][2]=='солодка вода'
    assert orders[0][3]=='з цукром'

@pytest.mark.database 
def test_table_count():
    db=Database()
    count = db.get_table_count()
    assert len(count) == 3

@pytest.mark.database 
def test_query_execution_speed():
    db=Database()
    start_time, end_time = db.execution_time_of_the_query()
    execution_time = end_time - start_time
    print(f"Час виконання запиту: {execution_time} секунд")

@pytest.mark.database
def test_new_comment_column():
    db= Database()
    db.new_column("comment","orders")
    query = "PRAGMA table_info(orders);"
    db.cursor.execute(query)
    columns = db.cursor.fetchall()
    column_names = [column[1] for column in columns]
    print("Назви колонок таблиці orders:", column_names)

@pytest.mark.database
def test_invalid_data_type_in_name_column():
    db = Database()
    with pytest.raises(Exception):
        db.insert_customer("12345") 

@pytest.mark.database
def test_modify_customer_data():
    db = Database()  
    original_data = db.select_customer_data("Sergii")

    customer_id = original_data[0] 
    new_address = "44 Halsey St"
    new_city = "New York"
    new_postal_code = "11216"
    new_country = "USA"
    db.modify_customer_data(customer_id, new_address, new_city, new_postal_code, new_country)

    modified_data = db.select_customer_data("Sergii")
    assert modified_data == (customer_id, new_address, new_city, new_postal_code, new_country)

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')
    assert user[0][0] == '44 Halsey St'

@pytest.mark.database
def test_delete_customer():
    db = Database()
    customer_name = "Stepan"  
    if db.customer_exists(customer_name):
        db.delete_customer(customer_name)
    assert not db.customer_exists(customer_name)

