import sys
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

sys.path.insert(0, '/opt/airflow/files/airflow_iguazio_spark-1.0-py3.8.egg')
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

    d2_d3_common_features = PythonOperator(task_id="d2_d3_common_features",
                                  python_callable=f.trigger_igz_spark,
                                  op_kwargs = {'igz_project': 'sparksimulation',
                                               'igz_function': 'igz_func_oppidreadyfill',
                                               'spark_package': 'modules',
                                               'spark_module': 'oppIdReadyFill',
                                               'spark_function' : 'd2_d3_common_features',
                                               'spark_function_param' : 'Monday'},
                                  provide_context=True
                                  )

    d3_not_in_prompt_list_at_pos = PythonOperator(task_id="d3_not_in_prompt_list_at_pos",
                                  python_callable=f.trigger_igz_spark,
                                  op_kwargs={'igz_project': 'sparksimulation',
                                             'igz_function': 'igz_func_oppidreadyfill',
                                             'spark_package': 'modules',
                                             'spark_module': 'oppIdReadyFill',
                                             'spark_function': 'd3_not_in_prompt_list_at_pos',
                                             'spark_function_param': 'Tuesday'},
                                  provide_context=True
                                  )

    end = DummyOperator(task_id="End")

    start >> d2_d3_common_features >> d3_not_in_prompt_list_at_pos >> end
