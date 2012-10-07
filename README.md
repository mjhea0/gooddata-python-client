GoodData API Client - Python
============================


Please note: This project is still in its early stages and is intended for *creating* a project on GoodData only. For help with *updating* a project, please see this video - http://www.youtube.com/watch?v=Cl5ZTvQSFLQ

Also, the original project can be found at https://github.com/mjhea0/gooddata-python

- Official GoodData API Docs: http://developer.gooddata.com/api/
- GoodData Apiary: http://docs.gooddata.apiary.io/


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


Wish List
-----------

1. Update client library to allow for *updating* a project.
2. Web App
3. Integration with MySQL
4. Simplify data modeling
5. Update documentation
6. Debugging/Cleaning
7. Supporting Incremental Load (multiple load interface?)

