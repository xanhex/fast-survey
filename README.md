# Fast Survey

Microservice for user surveys. It stores data in MongoDB database.

## Technologies

- Python
- FastAPI
- Asyncio
- PyMongo
- MongoDB
- Pytest
- Jinja2
- Bootstrap 5
- CSS
- Uvicorn
- Docker

## Standards

- pep8
- flake8
- black
- pymarkdown

## How to run

1. Clone the repository
2. To run on PostgreSQL instead of SQLite (default), put `.env` file into
`fastnames` folder with such content:

    ```env
    POSTGRES_DB=db_name
    POSTGRES_USER=db_user
    POSTGRES_PASSWORD=db_pswd
    DB_PORT=5432
    DATABASE_URL=postgresql+asyncpg://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres_db:${DB_PORT}/${POSTGRES_DB}
    ```

3. From the root folder run:

    ```bash
    docker compose up
    ```

## Local development and testing

1. Clone the project, activate virtual environment and install
dependencies from `fastnames/requirements.txt` file
2. To test the current functionality run `pytest` command

## TODO

1. Write tests
2. Update README
