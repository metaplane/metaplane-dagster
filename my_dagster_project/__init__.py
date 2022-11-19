import git
from .repository import my_dagster_project

git.Git("metaplane-dbt").clone("https://github.com/metaplane/metaplane-dbt.git")