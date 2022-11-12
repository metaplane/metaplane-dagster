from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(
        name="my_dagster_project",
        packages=find_packages(exclude=["my_dagster_project_tests"]),
        install_requires=[
            "dagster",
            "dagster_airflow",
            # See https://github.com/dagster-io/dagster/issues/2701
            "apache-airflow==1.10.10",
            # Conflicts with `Jinja2` which is used in dagster cli that dagster_airflow depends on
            "markupsafe<=2.0.1",
            "dagster-dbt",
            "dagster-fivetran"
        ],
        extras_require={"dev": ["dagit", "pytest"]},
    )