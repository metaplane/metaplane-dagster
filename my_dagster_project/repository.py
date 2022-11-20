import os

from dagster import define_asset_job, load_assets_from_package_module, repository, with_resources
from dagster_dbt import dbt_cli_resource
from my_dagster_project import assets
from .assets.fivetran_dbt_cloud_simple.fivetran_simple import fivetran_assets
from .assets.fivetran_dbt_cloud_simple.dbt_cloud_simple import my_dbt_cloud_job, basic_schedule
from .assets.dbt_core.dbt_core import dbt_assets, DBT_PROFILES, DBT_PROJECT_PATH, my_dbt_cli_job, dfe_schedule

@repository
def my_dagster_project():
    return [
        load_assets_from_package_module(assets),
        define_asset_job(name="all_assets_job"),
        fivetran_assets,
        my_dbt_cloud_job,
        basic_schedule,
        my_dbt_cli_job,
        dfe_schedule] + with_resources(
        dbt_assets, 
        resource_defs={
            # this resource is used to execute dbt cli commands
            "dbt": dbt_cli_resource.configured(
                {"project_dir": DBT_PROJECT_PATH, "profiles_dir": DBT_PROFILES}
                ),
            },
        )