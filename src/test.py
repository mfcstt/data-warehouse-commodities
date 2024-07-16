from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://postgres123:your_password@postgres.c58cacasojz8.us-east-2.rds.amazonaws.com:5432/your_database?sslmode=require"
engine = create_engine(DATABASE_URL)

# Testar a conexão
with engine.connect() as connection:
    result = connection.execute("SELECT 1")
    print(result.fetchone())