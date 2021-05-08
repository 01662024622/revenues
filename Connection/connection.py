from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


class Connection:
    @staticmethod
    def connection(db_url):
        engine = create_engine(db_url, connect_args={'connect_timeout': 150}, echo=True)
        return engine.connect()

    @staticmethod
    def dict2Object(d, v):
        for k in d.keys():
            setattr(v, k, d[k])
        return v
