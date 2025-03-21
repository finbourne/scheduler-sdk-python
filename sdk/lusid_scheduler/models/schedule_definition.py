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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictBool, StrictStr, conlist 
from lusid_scheduler.models.notification import Notification
from lusid_scheduler.models.resource_id import ResourceId
from lusid_scheduler.models.trigger import Trigger

class ScheduleDefinition(BaseModel):
    """
    Schedule  # noqa: E501
    """
    schedule_identifier: ResourceId = Field(..., alias="scheduleIdentifier")
    job_id: Optional[ResourceId] = Field(None, alias="jobId")
    name:  Optional[StrictStr] = Field(None,alias="name", description="A display name for this Schedule") 
    description:  Optional[StrictStr] = Field(None,alias="description", description="A description of the Schedule") 
    author:  Optional[StrictStr] = Field(None,alias="author", description="Name of the author of this schedule") 
    owner:  Optional[StrictStr] = Field(None,alias="owner", description="Name of owner of this schedule") 
    use_as_auth:  Optional[StrictStr] = Field(None,alias="useAsAuth", description="User to runs schedule when automatically run and authenticates   requests in the schedule") 
    arguments: Optional[Dict[str, StrictStr]] = Field(None, description="All arguments specified by this Schedule that will be passed in to the Job")
    trigger: Optional[Trigger] = None
    notifications: Optional[conlist(Notification)] = Field(None, description="Notifications for this Schedule")
    enabled: Optional[StrictBool] = Field(None, description="The status of this schedule")
    __properties = ["scheduleIdentifier", "jobId", "name", "description", "author", "owner", "useAsAuth", "arguments", "trigger", "notifications", "enabled"]

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
    def from_json(cls, json_str: str) -> ScheduleDefinition:
        """Create an instance of ScheduleDefinition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of schedule_identifier
        if self.schedule_identifier:
            _dict['scheduleIdentifier'] = self.schedule_identifier.to_dict()
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
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if author (nullable) is None
        # and __fields_set__ contains the field
        if self.author is None and "author" in self.__fields_set__:
            _dict['author'] = None

        # set to None if owner (nullable) is None
        # and __fields_set__ contains the field
        if self.owner is None and "owner" in self.__fields_set__:
            _dict['owner'] = None

        # set to None if use_as_auth (nullable) is None
        # and __fields_set__ contains the field
        if self.use_as_auth is None and "use_as_auth" in self.__fields_set__:
            _dict['useAsAuth'] = None

        # set to None if arguments (nullable) is None
        # and __fields_set__ contains the field
        if self.arguments is None and "arguments" in self.__fields_set__:
            _dict['arguments'] = None

        # set to None if notifications (nullable) is None
        # and __fields_set__ contains the field
        if self.notifications is None and "notifications" in self.__fields_set__:
            _dict['notifications'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ScheduleDefinition:
        """Create an instance of ScheduleDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ScheduleDefinition.parse_obj(obj)

        _obj = ScheduleDefinition.parse_obj({
            "schedule_identifier": ResourceId.from_dict(obj.get("scheduleIdentifier")) if obj.get("scheduleIdentifier") is not None else None,
            "job_id": ResourceId.from_dict(obj.get("jobId")) if obj.get("jobId") is not None else None,
            "name": obj.get("name"),
            "description": obj.get("description"),
            "author": obj.get("author"),
            "owner": obj.get("owner"),
            "use_as_auth": obj.get("useAsAuth"),
            "arguments": obj.get("arguments"),
            "trigger": Trigger.from_dict(obj.get("trigger")) if obj.get("trigger") is not None else None,
            "notifications": [Notification.from_dict(_item) for _item in obj.get("notifications")] if obj.get("notifications") is not None else None,
            "enabled": obj.get("enabled")
        })
        return _obj
