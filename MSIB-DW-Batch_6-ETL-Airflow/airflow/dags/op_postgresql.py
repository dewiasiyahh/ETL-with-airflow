import datetime
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator # type: ignore
from airflow.operators.empty import EmptyOperator 

with DAG(
    dag_id='op_postgres_example',
    start_date=datetime.datetime(2024, 5, 1),
    catchup=False,
    schedule_interval="@weekly"  # Set your desired schedule interval
) as dag:
    start = EmptyOperator(task_id= 'start', dag= dag) 


    # Create a pet table in the PostgreSQL database
    create_pet_table = PostgresOperator(
        task_id='create_pet_table',
        sql="""
            CREATE TABLE IF NOT EXISTS pet (
                pet_id SERIAL PRIMARY KEY,
                name VARCHAR NOT NULL,
                pet_type VARCHAR NOT NULL,
                birth_date DATE NOT NULL,
                owner VARCHAR NOT NULL
            );
        """,
        postgres_conn_id='postgres_default',  # Replace with your PostgreSQL connection ID
    )

    # Populate the pet table with sample data
    populate_pet_table = PostgresOperator(
        task_id='populate_pet_table',
        sql="sql/insert_pet.sql",  # Path to your SQL file containing INSERT statements
        postgres_conn_id='postgres_default',  # Replace with your PostgreSQL connection ID
    )
    end = EmptyOperator(task_id= 'end', dag= dag) 




# Set up task dependencies
start >> create_pet_table >>populate_pet_table  >> end
