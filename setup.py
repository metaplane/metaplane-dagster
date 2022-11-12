from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(
        name="fivetran_dbtcloud_simple",
        packages=find_packages(exclude=["fivetran_dbt_cloud_simple_tests"]),
        install_requires=[
            "dagster",
            "dagster-fivetran",
        ],
    )
