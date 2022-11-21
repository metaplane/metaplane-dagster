from dagster import job, ScheduleDefinition, file_relative_path, define_asset_job, AssetSelection
#from .fivetran_simple import fivetran_assets 
#let's see if we need this as in theory the sources in the dbt project should get mapped
from dagster_dbt import load_assets_from_dbt_project

DBT_PROJECT_PATH = file_relative_path(__file__, "../../../dbtproj")
DBT_PROFILES = file_relative_path(__file__, "../../resources")

dbt_assets = load_assets_from_dbt_project(project_dir=DBT_PROJECT_PATH, profiles_dir=DBT_PROFILES)

dfe_job = define_asset_job(name="dfe_job", selection=AssetSelection.keys("deal_flow_enriched").upstream() |
    AssetSelection.groups("hubspot"), tags={"type": "SDA_DFE_daily"})

dfe_schedule = ScheduleDefinition(job=dfe_job, cron_schedule="0 2 * * *")
