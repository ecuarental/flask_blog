"""These are the flask app settings."""


SECRET_KEY = 'you-will-never-guess'
DEBUG = True
DB_USERNAME = 'ecuarental'
DB_PASSWORD = '$alesforce!'
BLOG_DATABASE_NAME = 'blog'
DB_HOST = '127.0.0.1'
DB_URI = 'mysql+pymysql://%s:%s@%s/%s' % (DB_USERNAME, DB_PASSWORD, DB_HOST,
                                          BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
