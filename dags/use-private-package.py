from airflow_operator.hello_operator import SampleOperator
from airflow.operators.bash import BashOperator
from airflow import DAG


with DAG(
   "tutorial",
   tags=["example"],
) as dag:

    list_requirements = BashOperator(
        task_id="list_requirements",
        bash_commadn = "pip list"
    )

    sample_task = SampleOperator(task_id="sample-task", name="foo_bar")

    list_requirements >> sample_task