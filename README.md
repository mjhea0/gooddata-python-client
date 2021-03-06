GoodData API Client - Python
============================


Please note: This project is still in its early stages.

Also, the original project can be found at https://github.com/mjhea0/gooddata-python

- Official GoodData API Docs: http://developer.gooddata.com/api/
- GoodData Apiary: http://docs.gooddata.apiary.io/
- Official example of loading data vis REST API: http://developer.gooddata.com/advanced-guides/loading-data/loading-data-via-api


Example
------

Add your GoodData login information (email, password) to index_quotes_examples.py then execute the file

    from gooddataclient.connection import Connection
    from gooddataclient.project import Project
    from datasets.quotes import Quotes
  
    connection = Connection('email', 'password')
    proj_name = 'quotesFinal9242012'
    print '\n\n\nLoading Project: ', proj_name
    project = Project(connection).create(name=proj_name)
    project = Project(connection).load(name=proj_name)
    dataset = Quotes(project)
    dataset.upload()

Sample: http://www.youtube.com/watch?v=XxX70Wahb_Q&feature=plcp

    
Normal Usage
------------

Update the variables in the index, csv, and dataset files.

To do update your project with new data, add your new data to the CSV file, comment out this line in the index.py file-

    project = Project(connection).create(name=proj_name)

-and then execute the file.

Wish List
-----------

1. Simplying data loading process (dataset.py)
2. Web App
3. Integration with MySQL
4. Simplify data modeling
5. Update documentation
6. Debugging/Cleaning
7. Supporting Incremental Load (multiple load interface?)

