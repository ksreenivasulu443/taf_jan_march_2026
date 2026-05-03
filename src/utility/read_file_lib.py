from src.utility.helpers import read_schema,flatten

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
    elif file_type == 'json':
        if file_config['multiline']:
            df = spark.read.json(path=file_path,multiLine=file_config['multiline']==True )
            df.show()
            df = flatten(df)
        else:
            df = spark.read.json(path=file_path, multiLine=file_config['multiline'] == False)
            df = flatten(df)
    elif file_type == 'parquet':
        df = spark.read.parquet(file_path)
    elif file_type == 'avro':
        df = spark.read.format('avro').load(file_path)
    elif file_type == 'xml':
        df = spark.read.xml('avro').load(file_path)
    elif file_type == 'txt':
        df = (spark.read.csv(file_path,
                             header=file_config['header'],
                             sep=file_config['sep'],
                             inferSchema=file_config['inferSchema']))

    return df

#csv, json, parquet, avro, txt, xml