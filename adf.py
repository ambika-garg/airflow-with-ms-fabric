from datetime import datetime, timedelta

from airflow.models import DAG, BaseOperator
from airflow.providers.microsoft.azure.operators.data_factory import AzureDataFactoryRunPipelineOperator


with DAG(
    dag_id="example_adf_run_pipeline",
    start_date=datetime(2022, 5, 14),
    schedule_interval="@daily",
    catchup=False,
    default_args={
        "retries": 1,
        "retry_delay": timedelta(minutes=3),
        "azure_data_factory_conn_id": "azure_data_factory_conn_id", #This is a connection created on Airflow UI
    },
    default_view="graph",
) as dag:

    run_adf_pipeline = AzureDataFactoryRunPipelineOperator(
        task_id="run_adf_pipeline",
        pipeline_name="pipeline1", 
        parameters={"myParam": "value"},
    )

    run_adf_pipeline
