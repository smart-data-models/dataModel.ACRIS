from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import AnyUrl, BaseModel, Field, constr


class AirportElevationUnitOfMeasurement(BaseModel):
    Name: Optional[str] = Field(
        None,
        description='The name of the unit of measure for an Airport elevation above sea level.',
    )


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
    Srid: Optional[int] = Field(
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


class ZoneAreaLocation(BaseModel):
    Name: Optional[str] = Field(
        None, description='Unique name for the Zone Area Location.'
    )
    TerminalAreaLocation: Optional[TerminalAreaLocation] = Field(
        None,
        description='The geospatial or geopolitical location of an Airport Terminal building.',
    )


class Type(Enum):
    CheckpointAreaLocation = 'CheckpointAreaLocation'


class CheckpointAreaLocation(BaseModel):
    AirportElevation: Optional[AirportElevation] = Field(
        None, description='The height of an Airport, above sea level.'
    )
    Latitude: Optional[float] = Field(
        None, description='Coordinate of the latitude of the checkpoint area location.'
    )
    Longitude: Optional[float] = Field(
        None, description='Coordinate of the longitude of the checkpoint area location.'
    )
    Name: Optional[str] = Field(
        None,
        description='Unique name for geospatial or geopolitical location of a Checkpoint Area Location.',
    )
    Srid: Optional[float] = Field(
        None,
        description='A Spatial Reference System Identifier (SRID), to identify the spatial coordinate system definitions',
    )
    ZoneAreaLocation: Optional[ZoneAreaLocation] = Field(
        None,
        description='The geospatial or geopolitical location of a Queuing Zone in a Terminal.',
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
        None, description='It must be equal to CheckpointAreaLocation.'
    )
