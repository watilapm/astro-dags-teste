"""
teste
DAG auto-generated by Astro Cloud IDE.
"""

from airflow.decorators import dag
from astro import sql as aql
import pandas as pd
import pendulum


@aql.dataframe(task_id="python_1")
def python_1_func():
    print("teste de novo")

default_args={
    "owner": "watila portela machado,Open in Cloud IDE",
}

@dag(
    default_args=default_args,
    schedule="0 0 * * *",
    start_date=pendulum.from_format("2025-02-06", "YYYY-MM-DD").in_tz("UTC"),
    catchup=False,
    owner_links={
        "watila portela machado": "mailto:watilapm@gmail.com",
        "Open in Cloud IDE": "https://cloud.astronomer.io/cm6thfjc125ed01l0g5awm44f/cloud-ide/cm6tis6v125js01ivda2tyce6/cm6tkysyo271n01mdhevg37zs",
    },
)
def teste():
    python_1 = python_1_func()

dag_obj = teste()
