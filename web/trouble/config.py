import os

class Configuration(object):
	APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:lexbim95@localhost:5432/blog_db'
	#DB_PORT = os.environ['DB_PORT']
	#DB_USER = os.environ['POSTGRES_USER']
	#DB_PASS = os.environ['POSTGRES_PASS']
	#DB_NAME = os.environ['POSTGRES_DB']
	#DB_SERVICE = os.environ['DB_SERVICE']
	#DB_PORT = os.environ['DB_PORT']
	#SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
     #   DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
    #)