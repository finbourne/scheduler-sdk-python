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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, constr, validator
from lusid_scheduler.models.notification import Notification
from lusid_scheduler.models.resource_id import ResourceId
from lusid_scheduler.models.trigger import Trigger

class UpdateScheduleRequest(BaseModel):
    """
    Create a schedule definition  # noqa: E501
    """
    job_id: ResourceId = Field(..., alias="jobId")
    name: constr(strict=True, max_length=512, min_length=1) = Field(..., description="The updated name of the schedule")
    description: constr(strict=True, max_length=512, min_length=1) = Field(..., description="The updated description of the schedule")
    author: Optional[constr(strict=True, max_length=512, min_length=0)] = Field(None, description="The updated author of the schedule")
    owner: Optional[constr(strict=True, max_length=512, min_length=0)] = Field(None, description="The update owner of the schedule")
    arguments: Optional[Dict[str, StrictStr]] = Field(None, description="Updated arguments to be passed to the job  Note: The new arguments will completely replace old arguments")
    trigger: Optional[Trigger] = None
    notifications: conlist(Notification) = Field(..., description="Updated notifications for this schedule")
    enabled: Optional[StrictBool] = Field(None, description="Specify whether schedule is enabled or not  Defaults to true")
    use_as_auth: Optional[constr(strict=True, max_length=64, min_length=1)] = Field(None, alias="useAsAuth", description="Id of user associated with schedule. All calls to FINBOURNE services  as part of execution of this schedule will be authenticated as this   user. Can be null, in which case we'll default to that of the user   making this request")
    __properties = ["jobId", "name", "description", "author", "owner", "arguments", "trigger", "notifications", "enabled", "useAsAuth"]

    @validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
        return value

    @validator('description')
    def description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
        return value

    @validator('author')
    def author_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
        return value

    @validator('owner')
    def owner_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
        return value

    @validator('use_as_auth')
    def use_as_auth_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

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
    def from_json(cls, json_str: str) -> UpdateScheduleRequest:
        """Create an instance of UpdateScheduleRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of job_id
        if self.job_id:
            _dict['jobId'] = self.job_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of trigger
        if self.trigger:
            _dict['trigger'] = self.trigger.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in notifications (list)
        _items = []
        if self.notifications:
            for _item in self.notifications:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notifications'] = _items
        # set to None if author (nullable) is None
        # and __fields_set__ contains the field
        if self.author is None and "author" in self.__fields_set__:
            _dict['author'] = None

        # set to None if owner (nullable) is None
        # and __fields_set__ contains the field
        if self.owner is None and "owner" in self.__fields_set__:
            _dict['owner'] = None

        # set to None if arguments (nullable) is None
        # and __fields_set__ contains the field
        if self.arguments is None and "arguments" in self.__fields_set__:
            _dict['arguments'] = None

        # set to None if use_as_auth (nullable) is None
        # and __fields_set__ contains the field
        if self.use_as_auth is None and "use_as_auth" in self.__fields_set__:
            _dict['useAsAuth'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateScheduleRequest:
        """Create an instance of UpdateScheduleRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateScheduleRequest.parse_obj(obj)

        _obj = UpdateScheduleRequest.parse_obj({
            "job_id": ResourceId.from_dict(obj.get("jobId")) if obj.get("jobId") is not None else None,
            "name": obj.get("name"),
            "description": obj.get("description"),
            "author": obj.get("author"),
            "owner": obj.get("owner"),
            "arguments": obj.get("arguments"),
            "trigger": Trigger.from_dict(obj.get("trigger")) if obj.get("trigger") is not None else None,
            "notifications": [Notification.from_dict(_item) for _item in obj.get("notifications")] if obj.get("notifications") is not None else None,
            "enabled": obj.get("enabled"),
            "use_as_auth": obj.get("useAsAuth")
        })
        return _obj