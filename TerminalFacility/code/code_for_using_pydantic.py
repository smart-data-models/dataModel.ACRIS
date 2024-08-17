from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import AnyUrl, BaseModel, Field, constr


class AirportFacility(BaseModel):
    IataCode: Optional[str] = Field(
        None, description='Three character IATA code for the Airport.'
    )
    IcaoCode: Optional[str] = Field(
        None, description='Four character ICAO code for the Airport.'
    )
    Name: Optional[str] = Field(None, description='Common name of the Airport.')


class Type(Enum):
    TerminalFacility = 'TerminalFacility'


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
        None, description='It must be equal to TerminalFacility.'
    )
