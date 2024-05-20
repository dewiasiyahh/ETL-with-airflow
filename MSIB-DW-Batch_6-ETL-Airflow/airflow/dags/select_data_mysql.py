from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from airflow.providers.mysql.hooks.mysql import MySqlHook

def fetch_and_print_students():
    mysql_hook = MySqlHook(mysql_conn_id='mysql_conn')
    result = mysql_hook.get_records("SELECT * FROM students;")
    for row in result:
        print(row)

with DAG(
    dag_id='op_mysql_example',
    start_date=datetime(2024, 5, 1),
    catchup=False,
    schedule_interval="@daily"
) as dag:

    start = EmptyOperator(task_id='start')

    create_new_table = MySqlOperator(
        task_id='create_new_table',
        mysql_conn_id='mysql_conn',
        sql="CREATE TABLE IF NOT EXISTS students (student_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256));",
    )

    insert_data = MySqlOperator(
        task_id='insert_data',
        mysql_conn_id='mysql_conn',
        sql="INSERT INTO students (name) VALUES ('Alex Jones');",
    )

    fetch_data = PythonOperator(
        task_id='fetch_data',
        python_callable=fetch_and_print_students,
    )

    end = EmptyOperator(task_id='end')

start >> create_new_table >> insert_data >> fetch_data >> end