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

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist
from lusid_scheduler.models.scan_report import ScanReport
from lusid_scheduler.models.tag import Tag

class Image(BaseModel):
    """
    Represents the metadata of an image  # noqa: E501
    """
    name: Optional[StrictStr] = Field(None, description="Name of the image")
    push_time: Optional[datetime] = Field(None, alias="pushTime", description="The push time of the image")
    pull_time: Optional[datetime] = Field(None, alias="pullTime", description="The latest pull time of the image")
    digest: Optional[StrictStr] = Field(None, description="The digest of the image")
    size: Optional[StrictInt] = Field(None, description="The size of the image (in bytes)")
    tags: Optional[conlist(Tag)] = Field(None, description="The tags of the image")
    scan_report: Optional[ScanReport] = Field(None, alias="scanReport")
    __properties = ["name", "pushTime", "pullTime", "digest", "size", "tags", "scanReport"]

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
    def from_json(cls, json_str: str) -> Image:
        """Create an instance of Image from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item in self.tags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tags'] = _items
        # override the default output from pydantic by calling `to_dict()` of scan_report
        if self.scan_report:
            _dict['scanReport'] = self.scan_report.to_dict()
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if push_time (nullable) is None
        # and __fields_set__ contains the field
        if self.push_time is None and "push_time" in self.__fields_set__:
            _dict['pushTime'] = None

        # set to None if pull_time (nullable) is None
        # and __fields_set__ contains the field
        if self.pull_time is None and "pull_time" in self.__fields_set__:
            _dict['pullTime'] = None

        # set to None if digest (nullable) is None
        # and __fields_set__ contains the field
        if self.digest is None and "digest" in self.__fields_set__:
            _dict['digest'] = None

        # set to None if size (nullable) is None
        # and __fields_set__ contains the field
        if self.size is None and "size" in self.__fields_set__:
            _dict['size'] = None

        # set to None if tags (nullable) is None
        # and __fields_set__ contains the field
        if self.tags is None and "tags" in self.__fields_set__:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Image:
        """Create an instance of Image from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Image.parse_obj(obj)

        _obj = Image.parse_obj({
            "name": obj.get("name"),
            "push_time": obj.get("pushTime"),
            "pull_time": obj.get("pullTime"),
            "digest": obj.get("digest"),
            "size": obj.get("size"),
            "tags": [Tag.from_dict(_item) for _item in obj.get("tags")] if obj.get("tags") is not None else None,
            "scan_report": ScanReport.from_dict(obj.get("scanReport")) if obj.get("scanReport") is not None else None
        })
        return _obj
