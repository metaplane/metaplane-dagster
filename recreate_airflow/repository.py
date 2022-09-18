# start_repo_marker_0
from dagster_airflow.dagster_job_factory import make_dagster_job_from_airflow_dag
from recreate_airflow.airflow_complex_dag import main_airflow_dag

from dagster import repository

main_airflow_dag = make_dagster_job_from_airflow_dag(main_airflow_dag)

@repository
def with_airflow():
    return [main_airflow_dag]

# end_repo_marker_0

# start_repo_marker_1

airflow_simple_dag_with_execution_date = make_dagster_job_from_airflow_dag(
    dag=main_airflow_dag, tags={"airflow_execution_date": "2022-09-18 00:00:00"}
)
# end_repo_marker_1