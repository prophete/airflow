from airflow import DAG
from airflow.decorators import task
from datetime import datetime, timedelta

with DAG('map_expand', start_date=datetime(2023, 1, 1), schedule_interval=timedelta(seconds=10), catchup=False) as dag:

    @task
    def print_file(file: str):
        print(file)

    files = print_file.expand(file=["file_a", "file_b", "file_c"]) # Lancement en parrallele de 3 task identiques