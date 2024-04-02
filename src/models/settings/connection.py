from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
  def __init__(self) -> None:
    self.__connectionPath = "{}:///{}".format(
      "sqlite",
      "storage.db"
    )
    self.__engine=None
    self.__session=None
  
  def connectDb(self) -> None:
    self.__engine = create_engine(self.__connectionPath)
  
  def getEngine(self):
    return self.__engine

  def __enter__(self):
    sessionMaker = sessionmaker()
    self.__session = sessionMaker(bind=self.__engine)
    return self
  
  def __exit__(self):
    self.__session.close()

