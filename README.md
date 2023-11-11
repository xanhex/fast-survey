# Fast Survey

Microservice for user surveys. All user data is validated
before being stored in MongoDB database.

## Technologies

- Python
- FastAPI
- Asyncio
- PyMongo
- MongoDB
- Pytest
- Uvicorn
- Docker

## Standards

- pep8
- flake8
- mypy
- black
- pymarkdown

## How to run

1. Clone the repository
2. Put `.env` file into `fast_survey` folder with such content:

    ```env
    # API
    DATABASE_URL=mongodb://user:password@mongo:27017/
    DATABASE_URL_TEST=mongodb://user:password@localhost:27017/

    # MONGO
    MONGO_INITDB_ROOT_USERNAME=user
    MONGO_INITDB_ROOT_PASSWORD=password

    # ME
    ME_CONFIG_BASICAUTH_USERNAME=user
    ME_CONFIG_BASICAUTH_PASSWORD=password
    ME_CONFIG_MONGODB_URL=mongodb://user:password@mongo:27017/

    ```

3. From the root folder run:

    ```bash
    docker compose up
    ```

4. API Documentation - `http://localhost:8000/docs`
5. To run `pytest` tests activate virtual environment and install dependencies
   from `fast_survey/requirements.txt`

