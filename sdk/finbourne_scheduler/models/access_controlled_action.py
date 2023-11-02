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
from pydantic import BaseModel, Field, conlist, constr
from finbourne_scheduler.models.action_id import ActionId
from finbourne_scheduler.models.id_selector_definition import IdSelectorDefinition
from finbourne_scheduler.models.link import Link

class AccessControlledAction(BaseModel):
    """
    AccessControlledAction
    """
    description: constr(strict=True, min_length=1) = Field(...)
    action: ActionId = Field(...)
    limited_set: Optional[conlist(IdSelectorDefinition)] = Field(None, alias="limitedSet")
    links: Optional[conlist(Link)] = None
    __properties = ["description", "action", "limitedSet", "links"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> AccessControlledAction:
        """Create an instance of AccessControlledAction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of action
        if self.action:
            _dict['action'] = self.action.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in limited_set (list)
        _items = []
        if self.limited_set:
            for _item in self.limited_set:
                if _item:
                    _items.append(_item.to_dict())
            _dict['limitedSet'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if limited_set (nullable) is None
        # and __fields_set__ contains the field
        if self.limited_set is None and "limited_set" in self.__fields_set__:
            _dict['limitedSet'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccessControlledAction:
        """Create an instance of AccessControlledAction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccessControlledAction.parse_obj(obj)

        _obj = AccessControlledAction.parse_obj({
            "description": obj.get("description"),
            "action": ActionId.from_dict(obj.get("action")) if obj.get("action") is not None else None,
            "limited_set": [IdSelectorDefinition.from_dict(_item) for _item in obj.get("limitedSet")] if obj.get("limitedSet") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
