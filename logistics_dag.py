
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="logistics_etl_dag",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    ingest = BashOperator(
        task_id="ingest_to_s3",
        bash_command="python /path/to/ingestion/upload_to_s3.py"
    )

    etl = BashOperator(
        task_id="spark_etl",
        bash_command="spark-submit /path/to/spark_jobs/etl_job.py"
    )

    ingest >> etl
