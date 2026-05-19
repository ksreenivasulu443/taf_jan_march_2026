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



You are a Senior Python Architect, PySpark Engineer, ETL Automation Framework Reviewer, and QA Automation Expert.

Task:
Read and understand my complete ETL automation framework codebase written in Python, PySpark, and Pytest. Perform a deep architecture review and identify all possible issues, risks, and improvement areas.

Analysis scope:

1. Project Structure & Architecture
- Review folder structure and package organization
- Verify separation of concerns
- Detect tight coupling and duplicated logic
- Identify scalability and maintainability issues
- Check whether framework design follows modular architecture
- Suggest better structure if required

2. Python Coding Standards
- Verify PEP8 compliance
- Detect bad naming conventions
- Identify hardcoded values
- Find code smells
- Detect long functions and repeated code
- Check proper use of functions/classes
- Identify unnecessary imports
- Find dead or unreachable code
- Verify type hints usage
- Verify docstrings and comments
- Detect global variable misuse

3. PySpark Best Practices
- Detect inefficient transformations
- Find unnecessary actions (.count(), collect(), show())
- Detect repeated dataframe scans
- Check caching/persist usage
- Identify performance bottlenecks
- Detect improper joins
- Review partition strategy
- Review handling of null values
- Verify schema usage
- Detect expensive operations
- Suggest optimized code

4. Pytest Framework Review
- Analyze fixture usage
- Detect duplicate setup code
- Review conftest.py usage
- Verify parametrization
- Review assertion quality
- Check test isolation
- Detect dependency between tests
- Review pytest.ini configuration
- Review marker usage
- Detect flaky test risks

5. Logging Review
- Detect missing logging
- Verify logging levels
- Check log format consistency
- Detect print() statements
- Suggest enterprise logging implementation
- Identify missing exception logging
- Review log storage strategy

6. Exception Handling
- Detect missing try-except blocks
- Detect generic exception handling
- Verify error propagation
- Review custom exceptions
- Check failure reporting

7. Configuration Management
- Detect hardcoded paths
- Detect hardcoded credentials
- Review config files
- Review environment handling
- Verify secrets management

8. Reporting Framework
- Review report generation logic
- Verify failure reporting quality
- Review report readability
- Detect missing execution metrics
- Suggest improvements for ETL analysis

9. Performance Review
- Identify memory issues
- Detect redundant processing
- Detect repeated execution
- Suggest optimization opportunities
- Estimate performance impact

10. Code Quality Metrics
Provide:
- Maintainability score (1–10)
- Readability score (1–10)
- Scalability score (1–10)
- Testability score (1–10)
- Performance score (1–10)

11. Security Review
- Detect exposed credentials
- Detect unsafe file handling
- Detect SQL injection risks
- Detect unsafe dynamic execution
- Detect sensitive information exposure

12. Output format:

For every issue provide:

Issue Number:
Category:
Severity: Critical / High / Medium / Low
File Name:
Function/Class:
Problem:
Why this is a problem:
Recommended solution:
Example fixed code:

Finally provide:

1. Top 10 highest priority issues
2. Quick wins (can fix within 1 hour)
3. Medium effort improvements
4. Long-term architecture improvements
5. Suggested enterprise-grade folder structure
6. Overall framework summary
7. Refactored architecture recommendation

Do not give generic comments. Read actual code and provide file-level and function-level findings with examples.

