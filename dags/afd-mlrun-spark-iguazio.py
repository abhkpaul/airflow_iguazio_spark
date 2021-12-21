import sys
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

sys.path.insert(0, '/opt/airflow/dist/igz_func-1.0-py3.8.egg')
from func import remoteTrigger as f

default_args = {
    'owner': 'AIRFLOW',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

with DAG(dag_id='afd-airflow-spark-iguazio',
         start_date=datetime(2021, 12, 17),
         max_active_runs=3,
         schedule_interval='@daily',
         default_args=default_args,
         catchup=False
         ) as dag:
    start = DummyOperator(task_id="Start")

    sparkIgzTask = PythonOperator(task_id="sparkIgzTask",
                           python_callable=f.trigger_igz_spark,
                           op_kwargs={'project': 'sparksimulationab', 'function': 'igz_func_joba'},
                           provide_context=True
                           )

    end = DummyOperator(task_id="End")

    start >> sparkIgzTask >> end
