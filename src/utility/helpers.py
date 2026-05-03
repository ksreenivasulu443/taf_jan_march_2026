import os
from pyspark.sql.types import StructType
import json

def read_sql():
    pass


def read_schema(dir_path):
    schema_path = os.path.join(dir_path, 'schema.json')
    with open(schema_path, 'r') as f:
        schema = StructType.fromJson(json.load(f))
        print(("=="*100))
        print("schema path", schema_path)
        print("schema is", schema)
        print(("==" * 100))
    return schema