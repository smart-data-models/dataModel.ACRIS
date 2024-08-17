from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import AnyUrl, BaseModel, Field, constr


class Type(Enum):
    PassengerProcessType = 'PassengerProcessType'


class PassengerProcessType(BaseModel):
    Code: Optional[str] = Field(
        None, description='Unique code for the type of Passenger Party Process.'
    )
    Description: Optional[str] = Field(
        None, description='Description of the type of Passenger Party Process.'
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
        None, description='It must be equal to PassengerProcessType.'
    )
