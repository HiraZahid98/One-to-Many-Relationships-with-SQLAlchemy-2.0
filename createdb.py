from connect import engine
from models import Base, Program, Course

# print("getting metadata .....")
# print(Base.metadata)
Base.metadata.create_all(bind =engine)