#!/usr/bin/python3
"""this modules creates new engine DBStorage"""


from sqlalchemy import create_engine
from os import getenv

"""database values retrieved via environment variables"""
user = getenv("HBNB_MYSQL_USER")
passwd = getenv("HBNB_MYSQL_PWD")
host = getenv("HBNB_MYSQL_HOST")
db = getenv("HBNB_MYSQL_DB")
env = getenv("HBNB_MYSQL_HOST")


class DBStorage:
    """database class"""

    __engine = None
    __session = None

    def __init__(self):
        """linking the engine to the MySQL database and user created
        before (hbnb_dev and hbnb_dev_db)"""

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format
                                      (user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.dropall(self.__engine)

    def all(self, cls=None):
        """query condition """

    def new(self, obj):
        """add the object to the current database session"""

        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""

        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""

    def close(self):
        """"""
