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


class ZoneAreaLocation(BaseModel):
    Name: Optional[str] = Field(
        None, description='Unique name for the Zone Area Location.'
    )
    TerminalAreaLocation: Optional[TerminalAreaLocation] = Field(
        None,
        description='The geospatial or geopolitical location of an Airport Terminal building.',
    )


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
    Srid: Optional[int] = Field(
        None,
        description='A Spatial Reference System Identifier (SRID), to identify the spatial coordinate system definitions',
    )
    ZoneAreaLocation: Optional[ZoneAreaLocation] = Field(
        None,
        description='The geospatial or geopolitical location of a Queuing Zone in a Terminal.',
    )


class CheckpointFacilityOperatorParty(BaseModel):
    Name: Optional[str] = Field(
        None,
        description='Unique name of the Operator Party for the Checkpoint Facility.',
    )


class CheckpointFacilityType(BaseModel):
    Code: Optional[str] = Field(
        None, description='Unique code for the Checkpoint Facility Type.'
    )
    Description: Optional[str] = Field(
        None, description='Description of the Checkpoint Facility Type.'
    )


class AirportFacility(BaseModel):
    IataCode: Optional[str] = Field(
        None, description='Three character IATA code for the Airport.'
    )
    IcaoCode: Optional[str] = Field(
        None, description='Four character ICAO code for the Airport.'
    )
    Name: Optional[str] = Field(None, description='Common name of the Airport.')


class TerminalFacility(BaseModel):
    AirportFacility: Optional[AirportFacility] = Field(
        None,
        description='Information about an Airport as buildings or infrastructure used to provide services.',
    )
    Identifier: Optional[str] = Field(
        None, description='Unique identifier for the Terminal Facility.'
    )
    Name: Optional[str] = Field(
        None, description='Unique name for the Terminal Facility.'
    )


class ConcourseFacility(BaseModel):
    Identifier: Optional[str] = Field(
        None, description='Unique identifier for the Concourse Facility.'
    )
    Name: Optional[str] = Field(
        None, description='Unique name for the Concourse Facility.'
    )
    TerminalFacility: Optional[TerminalFacility] = Field(
        None,
        description='Information about an Airport Terminal as buildings or infrastructure used to provide services.',
    )


class OperationTimePeriod(BaseModel):
    ClosingTime: Optional[str] = Field(
        None,
        description='The date and time from when the Checkpoint Facility is closed. Date time should be UTC, compliant with ISO 8601 format (e.g. 2023-04-20T11:54:59Z)',
    )
    OpeningTime: Optional[str] = Field(
        None,
        description='The date and time from when the Checkpoint Facility is open. Date time should be UTC, compliant with ISO 8601 format (e.g. 2023-04-20T11:54:59Z)',
    )


class Type(Enum):
    CheckpointFacility = 'CheckpointFacility'


class CheckpointFacility(BaseModel):
    CheckpointAreaLocation: Optional[CheckpointAreaLocation] = Field(
        None, description='The geospatial or geopolitical location of a Checkpoint.'
    )
    CheckpointFacilityOperatorParty: Optional[CheckpointFacilityOperatorParty] = Field(
        None,
        description='Information that describes the Party responsible for the operation of a Checkpoint in an Airport.',
    )
    CheckpointFacilityType: Optional[CheckpointFacilityType] = Field(
        None,
        description='Information that describes the classification for a Checkpoint in an Airport. Values are: Security Screening, Customs.',
    )
    ConcourseFacility: Optional[ConcourseFacility] = Field(
        None,
        description='Information about an Airport Concourse as buildings or infrastructure used to provide services.',
    )
    Description: Optional[str] = Field(
        None, description='Description of the Checkpoint Facility.'
    )
    Identifier: Optional[str] = Field(
        None,
        description='Unique identifier for the Checkpoint Facility. The identifier should be unique within an Airport.',
    )
    Name: Optional[str] = Field(
        None,
        description='Unique name for the Checkpoint Facility. The name should be unique within an Airport.',
    )
    OperationTimePeriod: Optional[OperationTimePeriod] = Field(
        None, description='The time period over which the Checkpoint is operating.'
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
        None, description='It must be equal to CheckpointFacility.'
    )
