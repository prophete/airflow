from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import time


def hello_world():
    print("#############################################")
    print("  Hello, AIRFLOW!")
    print((datetime.now()+timedelta(hours=2)).strftime("%y-%m-%d %H:%M:%S"))
    print("#############################################")
    time.sleep(5)

# Define the DAG
dag = DAG(
    'every10s',
    description='A simple DAG that prints Hello, World!',
    start_date = datetime(2023,6,1),
    schedule_interval = timedelta(seconds=10),
    end_date=datetime(2023, 6, 1, hour=11, minute=2),
    catchup=False
)

# Define the task
hello_task = PythonOperator(
    task_id='hello_task',
    python_callable=hello_world,
    dag=dag
)

# Set the task dependencies
hello_task