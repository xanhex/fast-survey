"""Database settings and containters."""
from enum import Enum

from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, BeforeValidator, ConfigDict, Field
from typing_extensions import Annotated

from fast_survey import config

DATABASE_URL = config.Settings().database_url

PyObjectId = Annotated[str, BeforeValidator(str)]

client = AsyncIOMotorClient(DATABASE_URL)
db = client.fast_survey_database


class Gender(str, Enum):
    """Gender choice field."""

    male = 'male'
    female = 'female'


class Survey(BaseModel):
    """Container for a single user survey record."""

    id: PyObjectId | None = Field(alias='_id', default=None)
    name: str
    gender: Gender
    age: int = Field(gt=0, lt=150)
    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )
