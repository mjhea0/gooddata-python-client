GoodData API Client - Python
============================


Please note: This project is still in its early stages and is intended for *creating* a project on GoodData only. For help with *updating* a project, please see this video - http://www.youtube.com/watch?v=Cl5ZTvQSFLQ

Official GoodData API Docs: http://developer.gooddata.com/api/

GoodData Apiary: http://docs.gooddata.apiary.io/


Example
-----

Add your GoodData loging information (email, password) then execute the file

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