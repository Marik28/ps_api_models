from database import engine
from tables import Base

if __name__ == '__main__':
    Base.metadata.create_all(engine)
