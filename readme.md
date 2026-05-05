Step1 - source data, target data
        1.1 read source data
            1.1.1 file data
                    path, delimiter, header, schema, type,
                    access keys
            1.1.2 database
                    database creds, host, server,port, query/table,jars
            1.1.3 stream 
                    steam server details, topic
        1.2 read target data
            1.2.1 file data
                    path, delimiter, header, schema, type,
                    access keys
            1.2.2 database
                    database creds, host, server,port, query/table,jars
            1.2.3 stream 
                    steam server details, topic

2. validations
    1.count,duplicate, null,...dq
3. reporting

##conftest
##pytest.ini
#discovery test_table1- 1test & test_table2-2 test

# test1 
    looks for fixture - read_data
    looks for applied fixture inside read_data fixture(spark_session, read_config)
    spark_sessiom, its check any fixture - returns spark hand it over read_data fixture
    read_conif -- request, config data from config.yml will be read and pass it read_data
    once all fixture execute then it goes to test case
# test2









source:
  type: "database"
  transformation : ["N","NA"]
  table: "[dbo].[Customers]"
  env: "qa"
  exclude_cols: ['create_date','update_date']
target:
  type: "database"
  transformation : ["Y","SQL"]
  table: "[dbo].[Customers]"
  env: "qa"
  exclude_cols: ['create_date','update_date']

pytest -v -s table2/test_table2.py
1.pytest.init ( empty )
2. discovering the test methods - 1
3. runs conftest file
4. test_count(read_data) : starts executing
   read_data==>spark_session(spark),read_config(config_data), request ==>fixture
5. read_data









