from recreate_airflow.repository import main_airflow_dag

def test_main_airflow_dag():
    assert main_airflow_dag.execute_in_process()