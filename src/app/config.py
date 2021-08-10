class Config():
    #-------------------database connection------------
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@db/youtube'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'youtube'