import sqlalchemy as sql

from . models import Base

class DB:
	def __init__(self, dbfile):

		self.db_file = dbfile
		self._engine = None
		self._sesion = None

	@property
	def engine(self):
		if not self._engine:
			self._engine = sql.create_engine('sqlite:///{}'.format(self.db_file))

		return self._engine

	@property
	def session(self):
		if not self._session:
			self._session = sql.orm.sessionmaker()
			self._session.configure(bind=self.engine)

		return self._session

def create_database(db, clear=True):
	if clear:
		Base.metadata.drop_all(db.engine)
	Base.metadata.create_all(db.engine)

