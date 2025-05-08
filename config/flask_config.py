import os

env = os.getenv('FLASK_ENV')
debug = env == 'development'
