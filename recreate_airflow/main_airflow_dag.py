from datetime import timedelta

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.providers.dbt.cloud.operators.dbt import (
    DbtCloudRunJobOperator,
)
from fivetran_provider.operators.fivetran import FivetranOperator
from fivetran_provider.sensors.fivetran import FivetranSensor

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["david@metaplane.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

with DAG(
    "main",
    default_args=default_args,
    description="Metaplane main Airflow DAG",
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=["main"],
) as dag:

    stripe_sync = FivetranOperator(
        task_id="stripe-sync",
        connector_id="commitment_surprising",
    )

    stripe_sensor = FivetranSensor(
        task_id="stripe-sensor",
        connector_id="commitment_surprising",
        poke_interval=600,
    )

    hubspot_sync = FivetranOperator(
        task_id="hubspot-sync",
        connector_id="sociological_administrator",
    )

    hubspot_sensor = FivetranSensor(
        task_id="hubspot-sensor",
        connector_id="sociological_administrator",
        poke_interval=600,
    )

    linkedin_pages_sync = FivetranOperator(
        task_id="linkedin-pages-sync",
        connector_id="challenge_grieve",
    )

    linkedin_pages_sensor = FivetranSensor(
        task_id="linkedin-pages-sensor",
        connector_id="challenge_grieve",
        poke_interval=600,
    )

    trigger_dbt_cloud_job_run = DbtCloudRunJobOperator(
        task_id="trigger_dbt_cloud_job_run",
        job_id=117628,
        check_interval=10,
        timeout=300,
    )    

    stripe_sync >> stripe_sensor
    hubspot_sync >> hubspot_sensor
    linkedin_pages_sync >> linkedin_pages_sensor
    [stripe_sensor, hubspot_sensor, linkedin_pages_sensor] >> trigger_dbt_cloud_job_run
