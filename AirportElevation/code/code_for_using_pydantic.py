from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import AnyUrl, BaseModel, Field, constr


class AirportElevationUnitOfMeasurement(BaseModel):
    Name: Optional[str] = Field(
        None,
        description='The name of the unit of measure for an Airport elevation above sea level.',
    )


class Type(Enum):
    AirportElevation = 'AirportElevation'


class AirportElevation(BaseModel):
    AirportElevationUnitOfMeasurement: Optional[AirportElevationUnitOfMeasurement] = (
        Field(
            None,
            description='The unit of measure of the height of an Airport above sea level (FT for foot or M for metre).',
        )
    )
    Name: Optional[str] = Field(
        None, description='The name of an Airport elevation above sea level.'
    )
    Value: Optional[float] = Field(
        None, description='The value of an Airport elevation above sea level.'
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    type: Optional[Type] = Field(
        None, description='It must be equal to AirportElevation.'
    )
