# coding: utf-8

"""
    FINBOURNE Scheduler API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, Field, constr 

class TimeTrigger(BaseModel):
    """
    Time-based trigger  # noqa: E501
    """
    expression:  Optional[StrictStr] = Field(None,alias="expression", description="Cron expression") 
    time_zone:  Optional[StrictStr] = Field(None,alias="timeZone", description="Time zone of the Cron expression. If not provided, defaults to UTC") 
    __properties = ["expression", "timeZone"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TimeTrigger:
        """Create an instance of TimeTrigger from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if expression (nullable) is None
        # and __fields_set__ contains the field
        if self.expression is None and "expression" in self.__fields_set__:
            _dict['expression'] = None

        # set to None if time_zone (nullable) is None
        # and __fields_set__ contains the field
        if self.time_zone is None and "time_zone" in self.__fields_set__:
            _dict['timeZone'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TimeTrigger:
        """Create an instance of TimeTrigger from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TimeTrigger.parse_obj(obj)

        _obj = TimeTrigger.parse_obj({
            "expression": obj.get("expression"),
            "time_zone": obj.get("timeZone")
        })
        return _obj
