import os

from dagster import define_asset_job, load_assets_from_package_module, repository, with_resources

from my_dagster_project import assets
from .assets.fivetran_dbt_cloud_simple.fivetran_simple import fivetran_assets
from .assets.fivetran_dbt_cloud_simple.dbt_cloud_simple import my_dbt_cloud_job, basic_schedule


@repository
def my_dagster_project():
    return [
        load_assets_from_package_module(assets),
        define_asset_job(name="all_assets_job"),
        fivetran_assets,
        my_dbt_cloud_job,
        basic_schedule]

