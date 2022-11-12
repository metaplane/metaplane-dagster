from dagster_fivetran import fivetran_resource, load_assets_from_fivetran_instance

fivetran_instance = fivetran_resource.configured(
    {
        "api_key": {"env": "FIVETRAN_API_KEY"},
        "api_secret": {"env": "FIVETRAN_API_SECRET"},
    }
)
fivetran_assets = load_assets_from_fivetran_instance(fivetran_instance)


