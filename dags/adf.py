# from datetime import datetime, timedelta

# from airflow.models import DAG
# from airflow.providers.microsoft.azure.operators.data_factory import AzureDataFactoryRunPipelineOperator


# with DAG(
#     dag_id="example_adf_run_pipeline",
#     start_date=datetime(2022, 5, 14),
#     schedule_interval="@daily",
#     catchup=False,
#     default_args={
#         "retries": 1,
#         "retry_delay": timedelta(minutes=3),
#         "azure_data_factory_conn_id": "azure_data_factory_conn_id", #This is a connection created on Airflow UI
#     },
#     default_view="graph",
# ) as dag:

#     run_adf_pipeline = AzureDataFactoryRunPipelineOperator(
#         task_id="run_adf_pipeline",
#         pipeline_name="pipeline1",
#         parameters={"myParam": "value"},
#     )

#     run_adf_pipeline

# from airflow_operator.hello_operator import SampleOperator
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

    # sample_task = SampleOperator(task_id="sample-task", name="foo_bar")

    list_requirements