from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
        dag_id='dags_base_branch_operator',
        start_date=pendulum.datetime(2024, 6, 17, tz='Asia/Seoul'),
        schedule=None,
        catchup=False
) as dag:
    t1=BashOperator(
        task_id="t1",
        bash_command="exit 0",
        dag=dag
    )

    t2 = BashOperator(
        task_id="t2",
        bash_command="exit 1",
        dag=dag
    )

    t3 = BashOperator(
        task_id="t3",
        bash_command="exit 1",
        dag=dag
    )

    t4 = BashOperator(
        task_id="t4",
        bash_command="echo \"last task\"",
        trigger_rule='one_success',
        dag=dag
    )