from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import AnyUrl, BaseModel, Field, constr


class Type(Enum):
    AirportLocation = 'AirportLocation'


class AirportLocation(BaseModel):
    Latitude: Optional[float] = Field(
        None, description='Coordinate for latitude of the Airport.'
    )
    Longitude: Optional[float] = Field(
        None, description='Coordinate for longitude of the Airport.'
    )
    Name: Optional[str] = Field(
        None, description='Unique name for the Airport Location.'
    )
    Srid: Optional[float] = Field(
        None,
        description='A Spatial Reference System Identifier (SRID), to identify the spatial coordinate system definitions.',
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
        None, description='It must be equal to AirportLocation.'
    )
