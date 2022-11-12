from dagster_fivetran import fivetran_resource, load_assets_from_fivetran_instance

fivetran_instance = fivetran_resource.configured(
    {
        "api_key": "some_key",
        "api_secret": "some_secret",
    }
)
fivetran_assets = load_assets_from_fivetran_instance(fivetran_instance)


