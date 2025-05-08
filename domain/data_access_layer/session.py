from sqlalchemy.orm import sessionmaker

from domain.data_access_layer.engine import app_db_engine_provider


def session():
    session_factory = sessionmaker(bind=app_db_engine_provider.get_engine(),
                                   autoflush=False,
                                   autocommit=False)
    return session_factory()
