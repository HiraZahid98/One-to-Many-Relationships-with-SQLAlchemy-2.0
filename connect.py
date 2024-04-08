from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'sqlite:///site.db',
    echo=True
) 

# this is going to target specific database 

Session = sessionmaker(bind = engine)

db = Session()

# with engine.connect() as connection:
#     result = connection.execute(
#         text("SELECT 'hello'")
#     )
#     print(result.all())