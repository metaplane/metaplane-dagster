from dagster import job
from dagster_fivetran import fivetran_resource, fivetran_sync_op

my_fivetran_resource = fivetran_resource.configured(
    {
        "api_key": {"env": "FIVETRAN_API_KEY"},
        "api_secret": {"env": "FIVETRAN_API_SECRET"},
    }
)

sync_hubspot = fivetran_sync_op.configured({"connector_id": "sociological_administrator"}, name="sync_hubspot")
sync_linkedin_company_pages = fivetran_sync_op.configured({"connector_id": "challenge_grieve"}, name="sync_linkedin_company_pages")
sync_stripe = fivetran_sync_op.configured({"connector_id": "commitment_surprising"}, name="sync_stripe")

@job(resource_defs={"fivetran": my_fivetran_resource})
def my_simple_fivetran_job():
    sync_hubspot()
    sync_stripe()
    sync_linkedin_company_pages()
