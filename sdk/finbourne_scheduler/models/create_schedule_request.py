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
from finbourne_scheduler.models.notification import Notification
from finbourne_scheduler.models.resource_id import ResourceId
from finbourne_scheduler.models.trigger import Trigger

class CreateScheduleRequest(BaseModel):
    """
    Create a schedule definition  # noqa: E501
    """
    schedule_id: ResourceId = Field(..., alias="scheduleId")
    job_id: ResourceId = Field(..., alias="jobId")
    name: constr(strict=True, max_length=512, min_length=1) = Field(..., description="A display name for this Schedule")
    description: constr(strict=True, max_length=512, min_length=1) = Field(..., description="A description of the Schedule")
    author: Optional[constr(strict=True, max_length=512, min_length=0)] = Field(None, description="Name of the author of this schedule")
    owner: Optional[constr(strict=True, max_length=512, min_length=0)] = Field(None, description="Name of owner of this schedule")
    arguments: Optional[Dict[str, StrictStr]] = Field(None, description="All arguments specified by this Schedule that will be passed in to the Job")
    trigger: Optional[Trigger] = None
    notifications: conlist(Notification) = Field(..., description="Notifications for this Schedule")
    enabled: Optional[StrictBool] = Field(None, description="Specify whether schedule is enabled or not  Defaults to true")
    use_as_auth: Optional[constr(strict=True, max_length=64, min_length=1)] = Field(None, alias="useAsAuth", description="Id of user associated with schedule. All calls to FINBOURNE services  as part of execution of this schedule will be authenticated as this   user. Can be null, in which case we'll default to that of the user   making this request")
    __properties = ["scheduleId", "jobId", "name", "description", "author", "owner", "arguments", "trigger", "notifications", "enabled", "useAsAuth"]

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
    def from_json(cls, json_str: str) -> CreateScheduleRequest:
        """Create an instance of CreateScheduleRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of schedule_id
        if self.schedule_id:
            _dict['scheduleId'] = self.schedule_id.to_dict()
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
    def from_dict(cls, obj: dict) -> CreateScheduleRequest:
        """Create an instance of CreateScheduleRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateScheduleRequest.parse_obj(obj)

        _obj = CreateScheduleRequest.parse_obj({
            "schedule_id": ResourceId.from_dict(obj.get("scheduleId")) if obj.get("scheduleId") is not None else None,
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
