import yaml
from sqlalchemy import create_engine, text


def load_db_config():
    with open("config/db.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config


def create_db_connection():
    config = load_db_config()

    username = config["database_connection"]["username"]
    password = config["database_connection"]["password"]
    host = config["database_connection"]["host"]
    port = config["database_connection"]["port"]
    database = config["database_connection"]["database"]

    connection_string = (
        f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
    )
    engine = create_engine(connection_string)
    return engine


def main():
    engine = create_db_connection()

    try:
        with engine.connect() as conn:
            result = conn.execute(text("select 'hello world'"))
            print(result.all())
    except Exception as e:
        print(f"Error connecting to the database: {e}")


if __name__ == "__main__":
    main()
