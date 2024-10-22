from core.config import setting
from core.database import Session
from sqlalchemy import create_engine

engine = create_engine('sqlite:///sqldblite.db', echo=True)

def create_table():
    import models.__all_models
    
    setting.DBBaseModel.metadata.drop_all(engine)
    setting.DBBaseModel.metadata.create_all(engine)
    
    
if __name__=='__main__':
    create_table()