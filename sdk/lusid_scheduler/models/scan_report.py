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
from lusid_scheduler.models.scan_summary import ScanSummary
from lusid_scheduler.models.vulnerability import Vulnerability

class ScanReport(BaseModel):
    """
    Represents the details of a security scan of an image  # noqa: E501
    """
    severity: Optional[StrictStr] = Field(None, description="The overall severity. For example : \"High\" or \"None\"")
    status: Optional[StrictStr] = Field(None, description="The status of the report")
    start_time: Optional[datetime] = Field(None, alias="startTime", description="The start time of the scanning process")
    end_time: Optional[datetime] = Field(None, alias="endTime", description="The end time of the scanning process")
    scan_duration: Optional[StrictInt] = Field(None, alias="scanDuration", description="The duration of the scan in seconds")
    summary: Optional[ScanSummary] = None
    vulnerabilities: Optional[conlist(Vulnerability)] = Field(None, description="List of Finbourne.Scheduler.WebApi.Dtos.Images.Vulnerability")
    __properties = ["severity", "status", "startTime", "endTime", "scanDuration", "summary", "vulnerabilities"]

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
    def from_json(cls, json_str: str) -> ScanReport:
        """Create an instance of ScanReport from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of summary
        if self.summary:
            _dict['summary'] = self.summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in vulnerabilities (list)
        _items = []
        if self.vulnerabilities:
            for _item in self.vulnerabilities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vulnerabilities'] = _items
        # set to None if severity (nullable) is None
        # and __fields_set__ contains the field
        if self.severity is None and "severity" in self.__fields_set__:
            _dict['severity'] = None

        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

        # set to None if start_time (nullable) is None
        # and __fields_set__ contains the field
        if self.start_time is None and "start_time" in self.__fields_set__:
            _dict['startTime'] = None

        # set to None if end_time (nullable) is None
        # and __fields_set__ contains the field
        if self.end_time is None and "end_time" in self.__fields_set__:
            _dict['endTime'] = None

        # set to None if scan_duration (nullable) is None
        # and __fields_set__ contains the field
        if self.scan_duration is None and "scan_duration" in self.__fields_set__:
            _dict['scanDuration'] = None

        # set to None if vulnerabilities (nullable) is None
        # and __fields_set__ contains the field
        if self.vulnerabilities is None and "vulnerabilities" in self.__fields_set__:
            _dict['vulnerabilities'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ScanReport:
        """Create an instance of ScanReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ScanReport.parse_obj(obj)

        _obj = ScanReport.parse_obj({
            "severity": obj.get("severity"),
            "status": obj.get("status"),
            "start_time": obj.get("startTime"),
            "end_time": obj.get("endTime"),
            "scan_duration": obj.get("scanDuration"),
            "summary": ScanSummary.from_dict(obj.get("summary")) if obj.get("summary") is not None else None,
            "vulnerabilities": [Vulnerability.from_dict(_item) for _item in obj.get("vulnerabilities")] if obj.get("vulnerabilities") is not None else None
        })
        return _obj
