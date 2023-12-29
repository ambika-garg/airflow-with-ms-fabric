from airflow_operators.sampleOperator import SampleOperator
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    "create_private_package_as_requirement",
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
    },
    description="A simple tutorial DAG",
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["requirement"],
) as dag:

    list_requirements = BashOperator(
        task_id="list_requirements",
        bash_command = "pip list"
    )

    sample_task = SampleOperator(task_id="sample-task", name="foo_bar")

    list_requirements >> sample_task