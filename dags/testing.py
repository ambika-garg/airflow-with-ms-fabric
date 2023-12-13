from datetime import datetime, timedelta

from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator



with DAG(
    dag_id="testing",
    start_date=datetime(2022, 5, 14),
    schedule_interval="@daily",
    catchup=False,
    default_args={
        "retries": 1,
        "retry_delay": timedelta(minutes=3),
    },
    default_view="graph",
) as dag:

    list_requirements = BashOperator(
        task_id="bash_task",
        bash_command="pip list",
    )

    list_requirements
