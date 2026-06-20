import os
import yaml
import pytest
import importlib.util

from dotenv import load_dotenv
from pyspark.sql import SparkSession

from src.utility.read_file_lib import read_file
from src.utility.read_db_lib import read_db

#load local environment
load_dotenv()

# ============================================================
# Project Root
# ============================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


# ============================================================
# Execute Python Transformation
# ============================================================

def execute_python_transformation(
        file_path,
        spark,
        source_config,
        target_config):

    print("=" * 100)
    print(f"Executing Transformation File : {file_path}")
    print("=" * 100)

    spec = importlib.util.spec_from_file_location(
        "transformation_query",
        file_path
    )

    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)

    if not hasattr(module, "run_transformation"):
        raise AttributeError(
            """
            Transformation file must contain:
            
            def run_transformation(
                    spark,
                    source_config,
                    target_config):
                pass
            """
        )

    module.run_transformation(
        spark=spark,
        source_config=source_config,
        target_config=target_config
    )

    print("Transformation executed successfully")


# ============================================================
# Read Config Fixture
# ============================================================

@pytest.fixture(scope="module")
def read_config(request):

    print("This is read_config fixture")

    dir_path = request.node.fspath.dirname

    print("dir path", dir_path)

    config_path = os.path.join(
        dir_path,
        "config.yml"
    )

    print("config path", config_path)

    with open(config_path, "r") as f:
        config_data = yaml.safe_load(f)

    return config_data


# ============================================================
# Read Data Fixture
# ============================================================

@pytest.fixture(scope="module")
def read_data(spark_session, read_config, request):

    config_data = read_config
    spark = spark_session
    dir_path = request.node.fspath.dirname

    print("=" * 100)
    print("config data", config_data)
    print("=" * 100)

    source_config = config_data["source"]
    target_config = config_data["target"]

    # ========================================================
    # Source Data
    # ========================================================

    if source_config["type"].lower() == "database":

        transformation = source_config.get("transformation",["N", "NA"])
        transformation_enabled = transformation[0].upper() == "Y"
        transformation_type = transformation[1].lower()
        if transformation_enabled and transformation_type == "python":
            python_file_path = os.path.join(dir_path,"transformation_query.py")
            if not os.path.exists(python_file_path):
                raise FileNotFoundError(f"Transformation file not found: {python_file_path}")

            execute_python_transformation(
                file_path=python_file_path,
                spark=spark,
                source_config=source_config,
                target_config=target_config
            )

        source_df = read_db(
            spark=spark,
            config=source_config,
            dir_path=dir_path
        )

    else:

        source_df = read_file(
            spark=spark,
            file_type=source_config["type"],
            file_path=source_config["path"],
            file_config=source_config["file_config"],
            dir_path=dir_path
        )

    # ========================================================
    # Target Data
    # ========================================================

    if target_config["type"].lower() == "database":

        target_df = read_db(
            spark=spark,
            config=target_config,
            dir_path=dir_path
        )

    else:

        target_df = read_file(
            spark=spark,
            file_type=target_config["type"],
            file_path=target_config["path"],
            file_config=target_config["file_config"],
            dir_path=dir_path
        )

    return (
        source_df.drop(*source_config["exclude_cols"]),
        target_df.drop(*target_config["exclude_cols"])
    )


# ============================================================
# Spark Session Fixture - added by sreeni
# ============================================================

@pytest.fixture(scope="session")
def spark_session():

    taf_jan = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    azure_storage = os.path.join(
        taf_jan,
        "jars",
        "azure-storage-8.6.6.jar"
    )

    hadoop_azure = os.path.join(
        taf_jan,
        "jars",
        "hadoop-azure-3.3.1.jar"
    )

    sql_server = os.path.join(
        taf_jan,
        "jars",
        "mssql-jdbc-12.2.0.jre8.jar"
    )

    jar_path = ",".join([
        azure_storage,
        hadoop_azure,
        sql_server
    ])

    print("\nStarting Spark Session")
    print("Project Path :", taf_jan)
    print("Jar Path :", jar_path)

    spark = (
        SparkSession.builder
        .master("local[1]")
        .config("spark.jars", jar_path)
        .config("spark.driver.extraClassPath", jar_path)
        .config("spark.executor.extraClassPath", jar_path)
        .appName("ETL Automation FW")
        .getOrCreate()
    )

    print("Spark Version :", spark.version)

    adls_account_name = os.getenv(
        "ADLS_ACCOUNT_NAME"
    )

    key = os.getenv(
        "ADLS_TOKEN"
    )

    spark.conf.set(
        f"fs.azure.account.auth.type.{adls_account_name}.dfs.core.windows.net",
        "SharedKey"
    )

    spark.conf.set(
        f"fs.azure.account.key.{adls_account_name}.dfs.core.windows.net",
        key
    )

    yield spark

    print("\nStopping Spark Session")

    spark.stop()

def new_fixture():
    print("\nNew Fixture")