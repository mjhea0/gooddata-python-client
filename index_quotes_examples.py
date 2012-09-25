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

