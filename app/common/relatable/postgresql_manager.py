from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from app.common.relatable.session_manager import SessionManager
from app.config import POSTGRES_URL


class PostgresManager(SessionManager):
    def _create_session(self):
        postgres_url = POSTGRES_URL
        engine = create_engine(postgres_url)
        session_factory = sessionmaker(engine)

        return session_factory()
