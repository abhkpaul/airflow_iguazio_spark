import os
os.environ['MLRUN_DBPATH'] = 'https://mlrun-api.default-tenant.app.cvs-rx.iguazio-c0.com'
os.environ['MLRUN_ARTIFACT_PATH'] = '/User/artifacts/{{run.project}}'


import sys
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import mlrun
import mlrun.projects
from mlrun.api import schemas

def print_hello():
 return 'Hello Wolrd'

def main(**kwargs):
    mlrun.set_environment(project="sparksimulationrc")
    for k, v in kwargs.items():
        print(k, v)
    print("Here are the params: ", kwargs["params"])
    print(kwargs["params"]["p_mods"])

    mlrun.run_function("igz_spark_submit_rc3", params=kwargs["params"])

#if __name__ == '__main__': main()

default_args = {
    'owner': 'CVS',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

with DAG(dag_id='afd-airflow-spark-iguazio',
         start_date=datetime(2021, 12, 1),
         max_active_runs=3,
         schedule_interval='@daily',
         default_args=default_args,
         catchup=False
         ) as dag:

    task_test = PythonOperator(task_id="task_test",
                                  python_callable=print_hello)

    task_iguazio = PythonOperator(task_id="task_iguazio",
                                           python_callable=main,
                                  params={"p_mods": "mymod", "mods": "pyspark_test_2"},
                                  provide_context=True
                                  )

    task_test >> task_iguazio
