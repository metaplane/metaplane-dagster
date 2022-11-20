from dagster import job, ScheduleDefinition, file_relative_path, build_op_context
#from .fivetran_simple import fivetran_assets 
#let's see if we need this as in theory the sources in the dbt project should get mapped
from dagster_dbt import load_assets_from_dbt_project, dbt_cli_resource, dbt_build_op

DBT_PROJECT_PATH = file_relative_path(__file__, "../../../metaplane-dbt")
DBT_PROFILES = file_relative_path(__file__, "../../resources")

dbt_assets = load_assets_from_dbt_project(project_dir=DBT_PROJECT_PATH, profiles_dir=DBT_PROFILES)

dfe_dbt_cli_resource = dbt_cli_resource.configured(
                {"project_dir": DBT_PROJECT_PATH, "profiles_dir": DBT_PROFILES, "select": "deal_flow_enriched"}
                )

@job(resource_defs={"dbt":dfe_dbt_cli_resource}, tags={"type": "DFE_daily"})
def my_dbt_cli_job():
    dbt_build_op()

dfe_schedule = ScheduleDefinition(job=my_dbt_cli_job, cron_schedule="0 2 * * *")