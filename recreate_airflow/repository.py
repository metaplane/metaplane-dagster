# start_repo_marker_0
from dagster_airflow.dagster_job_factory import make_dagster_job_from_airflow_dag
from recreate_airflow.main_airflow_dag import dag

from dagster import repository

airflow_main_airflow_dag = make_dagster_job_from_airflow_dag(dag)

@repository
def recreate_airflow():
    return [airflow_main_airflow_dag]

# end_repo_marker_0