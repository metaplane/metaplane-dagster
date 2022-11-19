from dagster import job, ScheduleDefinition, file_relative_path
#from .fivetran_simple import fivetran_assets 
#let's see if we need this as in theory the sources in the dbt project should get mapped
from dagster_dbt import load_assets_from_dbt_project

DBT_PROFILES = file_relative_path(__file__, "../../resources")

dbt_assets = load_assets_from_dbt_project(project_dir="https://github.com/metaplane/metaplane-dbt",
    profiles_dir=DBT_PROFILES)