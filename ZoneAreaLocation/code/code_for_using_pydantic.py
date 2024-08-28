from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import AnyUrl, BaseModel, Field, constr


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


class TerminalAreaLocation(BaseModel):
    AirportLocation: Optional[AirportLocation] = Field(
        None, description='The geospatial or geopolitical location of an Airport.'
    )
    Name: Optional[str] = Field(
        None, description='Unique name for the Terminal Area Location.'
    )


class Type(Enum):
    ZoneAreaLocation = 'ZoneAreaLocation'


class ZoneAreaLocation(BaseModel):
    Name: Optional[str] = Field(
        None, description='Unique name for the Zone Area Location.'
    )
    TerminalAreaLocation: Optional[TerminalAreaLocation] = Field(
        None,
        description='The geospatial or geopolitical location of an Airport Terminal building.',
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
        None, description='It must be equal to ZoneAreaLocation.'
    )