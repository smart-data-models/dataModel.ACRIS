from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import AnyUrl, BaseModel, Field, constr


class Type(Enum):
    MeasurementDeviceLocation = 'MeasurementDeviceLocation'


class MeasurementDeviceLocation(BaseModel):
    Name: Optional[str] = Field(
        None, description='Unique name for the location of the Measurement Device.'
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
        None, description='It must be equal to MeasurementDeviceLocation.'
    )