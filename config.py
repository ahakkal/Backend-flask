# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
#basedir = os.path.abspath(os.path.dirname(__file__))
# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'mysql://admin:admin@localhost/PFA'

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

