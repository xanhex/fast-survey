"""
Fast Survey app.

Microservice for user surveys.
"""
from collections import Counter
from functools import lru_cache

from fastapi import Depends, FastAPI, status
from pydantic import BaseModel, ConfigDict

from fast_survey.config import settings
from fast_survey.database import Survey, db_init

app = FastAPI()


@lru_cache
def survey_collection():
    """Database initialization."""
    return db_init(settings.database_url).surveys


class Report(BaseModel):
    """Survey report."""

    genders: dict[str, int]
    ages: dict[int, int]
    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )


@app.get(
    '/',
    summary='Statistic',
    response_model=Report,
)
async def users_surveys(surveys=Depends(survey_collection)) -> Report:
    """Get statistics of user surveys."""
    all_surveys: list[dict] = await surveys.find().to_list(None)
    result: dict[str, Counter] = {'ages': Counter(), 'genders': Counter()}
    for survey in all_surveys:
        result['ages'].update([survey['age']])
        result['genders'].update([survey['gender']])
    return Report(**result)


@app.post(
    '/create_survey/',
    summary='Create user survey',
    response_model=Survey,
    status_code=status.HTTP_201_CREATED,
)
async def create_user_survey(
    survey: Survey,
    surveys=Depends(survey_collection),
) -> Survey | None:
    """Add new user survey."""
    new_survey = await surveys.insert_one(
        survey.model_dump(by_alias=True, exclude={'id'}),
    )
    return await surveys.find_one({'_id': new_survey.inserted_id})
