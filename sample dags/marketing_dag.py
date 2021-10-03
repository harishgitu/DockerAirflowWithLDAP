from airflow import DAG
from airflow.operators.dummy import DummyOperator

from datetime import datetime

default_args = {
    'start_date': datetime(2021, 1, 1)
}

with DAG('mktg_dag', tags=['marketing'], schedule_interval='@daily', 
    default_args=default_args, catchup=False) as dag:

    task_a = DummyOperator(
        task_id="task_a"
    )