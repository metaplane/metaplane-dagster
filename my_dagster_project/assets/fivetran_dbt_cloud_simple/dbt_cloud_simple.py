from dagster import job
from dagster_dbt import dbt_cloud_resource, dbt_cloud_run_op

# configure an operation to run the specific job
run_dbt_nightly_sync = dbt_cloud_run_op.configured(
    {"job_id": 117628}, name="run_dbt_nightly_sync"
)

# configure a resource to connect to your dbt Cloud instance
my_dbt_cloud_resource = dbt_cloud_resource.configured(
    {"auth_token": {"env": "DBT_CLOUD_AUTH_TOKEN"}, "account_id": 6494}
)

# create a job that uses your op and resource
@job(resource_defs={"dbt_cloud": my_dbt_cloud_resource})
def my_dbt_cloud_job():
    run_dbt_nightly_sync()