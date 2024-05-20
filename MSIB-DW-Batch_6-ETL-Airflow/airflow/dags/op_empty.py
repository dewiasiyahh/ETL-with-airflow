from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 1, 1),
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='op_empty_example', 
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False, 
) as dag:
    first_task = EmptyOperator(task_id='start')
    last_task = EmptyOperator(task_id='end')

    other_tasks = EmptyOperator(task_id='other')

    first_task >> other_tasks >> last_task
