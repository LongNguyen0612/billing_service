import logging
from sqlalchemy.orm import Session

from app.common.relatable import PostgresManager
from ._side_effected import SideEffectedAppended, SideEffected

log = logging.getLogger(__name__)


class PostgresSessionCreator(SideEffectedAppended):
    def __init__(self, side_effect: SideEffected,
                 error: Exception = None):
        side_effect.add_side_effected(self)
        self.session: Session = PostgresManager().session

        self.__exception = error
        if self.__exception:
            log.debug('Exception on SQL error %s', str(self.__exception))

    def commit(self):
        self.session.commit()
        log.info('Commit and close Postgres transaction')
        self.session.close()

    def reset(self, exception):
        self.session.rollback()
        log.info('Rollback and close Postgres transaction')
        self.session.close()
