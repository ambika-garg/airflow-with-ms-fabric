from airflow_operator.hello_operator import SampleOperator
from airflow import DAG


with DAG(
   "tutorial",
   tags=["example"],
) as dag:
    sample_task = SampleOperator(task_id="sample-task", name="foo_bar")

    sample_task