from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

# Define the base class for SQLAlchemy models
Base = declarative_base()

class PostgresPipeline(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(255))
    product_price = Column(String(50))
    product_image_url = Column(Text)
    product_link = Column(Text)
    
# Setup database connection function
def setup_database():
    db_user = 'scrapyuser'
    db_password = 'scrapypassword'
    db_host = 'postgres'
    db_port = 5432
    db_name = 'scrapydb'

    # Database URL for PostgreSQL
    database_url = f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    engine = create_engine(database_url)
    
    # Create all tables (if they don't exist)
    Base.metadata.create_all(engine)

# Call setup_database at the start of your pipeline
setup_database()
