import os
from pyspark.sql.types import *
import json
from pyspark.sql.functions import col, explode_outer

def read_query(dir_path):
    query_path = os.path.join(dir_path, 'transformation_query.sql')
    with open(query_path, 'r') as f:
        query= f.read()
    return query



def read_schema(dir_path):
    schema_path = os.path.join(dir_path, 'schema.json')
    with open(schema_path, 'r') as f:
        schema = StructType.fromJson(json.load(f))
        print(("=="*100))
        print("schema path", schema_path)
        print("schema is", schema)
        print(("==" * 100))
    return schema

def flatten(df):
    # compute Complex Fields (Lists and Structs) in Schema
    complex_fields = dict([(field.name, field.dataType)
                           for field in df.schema.fields
                           if type(field.dataType) == ArrayType or type(field.dataType) == StructType])
    while len(complex_fields) != 0:
        col_name = list(complex_fields.keys())[0]
        print("Processing :" + col_name + " Type : " + str(type(complex_fields[col_name])))

        # if StructType then convert all sub element to columns.
        # i.e. flatten structs
        if type(complex_fields[col_name]) == StructType:
            expanded = [col(col_name + '.' + k).alias(col_name + '_' + k) for k in
                        [n.name for n in complex_fields[col_name]]]
            df = df.select("*", *expanded).drop(col_name)

        # if ArrayType then add the Array Elements as Rows using the explode function
        # i.e. explode Arrays
        elif type(complex_fields[col_name]) == ArrayType:
            df = df.withColumn(col_name, explode_outer(col_name))

        # recompute remaining Complex Fields in Schema
        complex_fields = dict([(field.name, field.dataType)
                               for field in df.schema.fields
                               if type(field.dataType) == ArrayType or type(field.dataType) == StructType])
    return df