from app.common.relatable._relatable import Relatable
from abc import ABC, abstractmethod
from sqlalchemy.orm import Session


class SessionManager(Relatable, ABC):
    def __init__(self, session=None):
        """
        Create SQLAlchemy session and provide management methods

        :param session: For parsing external session. If None, create session according to req_slave.
        :param req_slave: if True return session to slave db that available only for reading.
                          if False return session to master db that available for reading and writing.
        """
        if not session:
            session = self._create_session()
        self.session: Session = session

        # Some methods help reduce call session directly

    def commit(self):
        self.session.commit()

    def close(self):
        self.session.close()

    def rollback(self):
        self.session.rollback()

    def flush(self):
        self.session.flush()

    def get_session(self):
        return self.session

    @abstractmethod
    def _create_session(self):
        pass
