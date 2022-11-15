from dagster import job, ScheduleDefinition
from dagster_dbt import dbt_cloud_resource, dbt_cloud_run_op
from .fivetran_simple import sync_hubspot, sync_linkedin_company_pages, sync_stripe, fivetran_instance

# configure an operation to run the specific job
run_dbt_nightly_sync = dbt_cloud_run_op.configured(
    {"job_id": 117628}, name="run_dbt_nightly_sync"
)

# configure a resource to connect to your dbt Cloud instance
my_dbt_cloud_resource = dbt_cloud_resource.configured(
    {"auth_token": {"env": "DBT_CLOUD_AUTH_TOKEN"}, "account_id": 6494}
)

# create a job that uses your op and resource
@job(resource_defs={"dbt_cloud": my_dbt_cloud_resource, "fivetran": fivetran_instance}, tags={"type": "main_daily"})
def my_dbt_cloud_job():
    run_dbt_nightly_sync(start_after=[sync_stripe(), sync_hubspot(), sync_linkedin_company_pages()])

basic_schedule = ScheduleDefinition(job=my_dbt_cloud_job, cron_schedule="0 0 * * *")