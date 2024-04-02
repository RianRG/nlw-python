from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class __DBConnectionHandler:
  def __init__(self) -> None:
    self.__connectionPath = "{}:///{}".format(
      "sqlite",
      "storage.db"
    )
    self.__engine=None
    self.session=None
  
  def connectDb(self) -> None:
    self.__engine = create_engine(self.__connectionPath)
  
  def getEngine(self):
    return self.__engine

  def __enter__(self):
    sessionMaker = sessionmaker()
    self.session = sessionMaker(bind=self.__engine)
    return self
  
  def __exit__(self, exc_type, exc_val, exc_tb):
    self.session.close()

dbConnectionHandler = __DBConnectionHandler()