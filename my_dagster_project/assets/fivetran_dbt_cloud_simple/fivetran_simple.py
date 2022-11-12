from dagster import job, asset
from dagster_fivetran import fivetran_resource, load_assets_from_fivetran_instance, fivetran_sync_op

fivetran_instance = fivetran_resource.configured(
    {
        "api_key": {"env": "FIVETRAN_API_KEY"},
        "api_secret": {"env": "FIVETRAN_API_SECRET"},
    }
)

fivetran_assets = load_assets_from_fivetran_instance(fivetran_instance)

sync_hubspot = fivetran_sync_op.configured({"connector_id": "sociological_administrator"}, name="sync_hubspot")
sync_linkedin_company_pages = fivetran_sync_op.configured({"connector_id": "challenge_grieve"}, name="sync_linkedin_company_pages")
sync_stripe = fivetran_sync_op.configured({"connector_id": "commitment_surprising"}, name="sync_stripe")