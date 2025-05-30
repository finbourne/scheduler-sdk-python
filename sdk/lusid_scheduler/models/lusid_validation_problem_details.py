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


from typing import Any, Dict, List, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictInt, StrictStr, conlist, constr 

class LusidValidationProblemDetails(BaseModel):
    """
    LusidValidationProblemDetails
    """
    name:  StrictStr = Field(...,alias="name") 
    error_details: Optional[conlist(Dict[str, StrictStr])] = Field(None, alias="errorDetails")
    code: StrictInt = Field(...)
    errors: Optional[Dict[str, conlist(StrictStr)]] = None
    type:  Optional[StrictStr] = Field(None,alias="type") 
    title:  Optional[StrictStr] = Field(None,alias="title") 
    status: Optional[StrictInt] = None
    detail:  Optional[StrictStr] = Field(None,alias="detail") 
    instance:  Optional[StrictStr] = Field(None,alias="instance") 
    __properties = ["name", "errorDetails", "code", "errors", "type", "title", "status", "detail", "instance"]

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
    def from_json(cls, json_str: str) -> LusidValidationProblemDetails:
        """Create an instance of LusidValidationProblemDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in errors (dict of array)
        _field_dict_of_array = {}
        if self.errors:
            for _key in self.errors:
                if self.errors[_key]:
                    _field_dict_of_array[_key] = [
                        _item.to_dict() for _item in self.errors[_key]
                    ]
            _dict['errors'] = _field_dict_of_array
        # set to None if error_details (nullable) is None
        # and __fields_set__ contains the field
        if self.error_details is None and "error_details" in self.__fields_set__:
            _dict['errorDetails'] = None

        # set to None if errors (nullable) is None
        # and __fields_set__ contains the field
        if self.errors is None and "errors" in self.__fields_set__:
            _dict['errors'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if title (nullable) is None
        # and __fields_set__ contains the field
        if self.title is None and "title" in self.__fields_set__:
            _dict['title'] = None

        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

        # set to None if detail (nullable) is None
        # and __fields_set__ contains the field
        if self.detail is None and "detail" in self.__fields_set__:
            _dict['detail'] = None

        # set to None if instance (nullable) is None
        # and __fields_set__ contains the field
        if self.instance is None and "instance" in self.__fields_set__:
            _dict['instance'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LusidValidationProblemDetails:
        """Create an instance of LusidValidationProblemDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LusidValidationProblemDetails.parse_obj(obj)

        _obj = LusidValidationProblemDetails.parse_obj({
            "name": obj.get("name"),
            "error_details": obj.get("errorDetails"),
            "code": obj.get("code"),
            "errors": obj.get("errors"),
            "type": obj.get("type"),
            "title": obj.get("title"),
            "status": obj.get("status"),
            "detail": obj.get("detail"),
            "instance": obj.get("instance")
        })
        return _obj
