from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Database(object):
    def __init__(self, database_file, application):
        self.application = application
        self.engine = create_engine(database_file, convert_unicode=True, echo=False)
        self.db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=self.engine))
        Base.query = self.db_session.query_property()

        self._init_db()

    def _init_db(self):
        self.application.logger.info('Attempting to initialise database')

        import flaskapi.models.user
        Base.metadata.create_all(bind=self.engine)

        self.application.logger.info('Database initialised successfully')
