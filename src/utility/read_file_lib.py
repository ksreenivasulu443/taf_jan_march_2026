from src.utility.helpers import read_schema

def read_file(spark, file_type, file_path,file_config,dir_path):
    file_type = file_type.lower()
    if file_type == 'csv':
        if file_config['schema'] =='Y':
            schema = read_schema(dir_path)
            df = (spark.read.schema(schema).
                  csv(file_path,
                      header=file_config['header'],
                      sep=file_config['sep']))
        else:
            df = (spark.read.csv(file_path,
                                 header=file_config['header'],
                                 sep=file_config['sep'],
                                 inferSchema=file_config['inferSchema']))
    return df

#csv, json, parquet, avro, txt, xml