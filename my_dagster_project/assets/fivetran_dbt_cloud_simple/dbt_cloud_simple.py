from dagster import job
from dagster_dbt import dbt_cloud_resource, dbt_cloud_run_op
from .fivetran_simple import sync_hubspot, sync_linkedin_company_pages, sync_stripe

# configure an operation to run the specific job
run_dbt_nightly_sync = dbt_cloud_run_op.configured(
    {"job_id": 33333}, name="run_dbt_nightly_sync"
)

# configure a resource to connect to your dbt Cloud instance
my_dbt_cloud_resource = dbt_cloud_resource.configured(
    {"auth_token": {"env": "DBT_CLOUD_AUTH_TOKEN"}, "account_id": 11111}
)

# create a job that uses your op and resource
@job(resource_defs={"dbt_cloud": my_dbt_cloud_resource})
def my_dbt_cloud_job():
    run_dbt_nightly_sync(start_after=[sync_stripe(), sync_hubspot(), sync_linkedin_company_pages()])