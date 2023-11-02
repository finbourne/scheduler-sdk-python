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
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from finbourne_scheduler.models.argument_definition import ArgumentDefinition
from finbourne_scheduler.models.required_resources import RequiredResources
from finbourne_scheduler.models.resource_id import ResourceId

class JobDefinition(BaseModel):
    """
    Definition of a job  # noqa: E501
    """
    job_id: ResourceId = Field(..., alias="jobId")
    name: Optional[StrictStr] = Field(None, description="Name of the job")
    author: Optional[StrictStr] = Field(None, description="Author of the job")
    date_created: Optional[datetime] = Field(None, alias="dateCreated", description="Date when job was created")
    description: Optional[StrictStr] = Field(None, description="Description of this job")
    docker_image: Optional[StrictStr] = Field(None, alias="dockerImage", description="Information about the docker image in the format “image_source/image_name:image_tag”")
    ttl: Optional[StrictInt] = Field(None, description="Time To Live of the job run in seconds  Defaults to 5 minutes(300)")
    min_cpu: Optional[StrictStr] = Field(None, alias="minCpu", description="Specifies  minimum number of CPUs to be allocated for the job  Default to 2")
    max_cpu: Optional[StrictStr] = Field(None, alias="maxCpu", description="Specifies  maximum number of CPUs to be allocated for the job")
    min_memory: Optional[StrictStr] = Field(None, alias="minMemory", description="Specifies the minimum amount of memory (in GiB) to be allocated for the job")
    max_memory: Optional[StrictStr] = Field(None, alias="maxMemory", description="Specifies the maximum amount of memory (in GiB) to be allocated for the job")
    argument_definitions: Optional[Dict[str, ArgumentDefinition]] = Field(None, alias="argumentDefinitions", description="All arguments for this job to run")
    command_line_argument_separator: Optional[StrictStr] = Field(None, alias="commandLineArgumentSeparator", description="Value to separate command line arguments  e.g : If a job has a command line argument named 'folder' and the runtime value is 's3://path' then this  would be supplied to the command as 'folder{separatorValue}s3://path'  Default to a space")
    required_resources: RequiredResources = Field(..., alias="requiredResources")
    __properties = ["jobId", "name", "author", "dateCreated", "description", "dockerImage", "ttl", "minCpu", "maxCpu", "minMemory", "maxMemory", "argumentDefinitions", "commandLineArgumentSeparator", "requiredResources"]

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
    def from_json(cls, json_str: str) -> JobDefinition:
        """Create an instance of JobDefinition from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in argument_definitions (dict)
        _field_dict = {}
        if self.argument_definitions:
            for _key in self.argument_definitions:
                if self.argument_definitions[_key]:
                    _field_dict[_key] = self.argument_definitions[_key].to_dict()
            _dict['argumentDefinitions'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of required_resources
        if self.required_resources:
            _dict['requiredResources'] = self.required_resources.to_dict()
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if author (nullable) is None
        # and __fields_set__ contains the field
        if self.author is None and "author" in self.__fields_set__:
            _dict['author'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if docker_image (nullable) is None
        # and __fields_set__ contains the field
        if self.docker_image is None and "docker_image" in self.__fields_set__:
            _dict['dockerImage'] = None

        # set to None if min_cpu (nullable) is None
        # and __fields_set__ contains the field
        if self.min_cpu is None and "min_cpu" in self.__fields_set__:
            _dict['minCpu'] = None

        # set to None if max_cpu (nullable) is None
        # and __fields_set__ contains the field
        if self.max_cpu is None and "max_cpu" in self.__fields_set__:
            _dict['maxCpu'] = None

        # set to None if min_memory (nullable) is None
        # and __fields_set__ contains the field
        if self.min_memory is None and "min_memory" in self.__fields_set__:
            _dict['minMemory'] = None

        # set to None if max_memory (nullable) is None
        # and __fields_set__ contains the field
        if self.max_memory is None and "max_memory" in self.__fields_set__:
            _dict['maxMemory'] = None

        # set to None if argument_definitions (nullable) is None
        # and __fields_set__ contains the field
        if self.argument_definitions is None and "argument_definitions" in self.__fields_set__:
            _dict['argumentDefinitions'] = None

        # set to None if command_line_argument_separator (nullable) is None
        # and __fields_set__ contains the field
        if self.command_line_argument_separator is None and "command_line_argument_separator" in self.__fields_set__:
            _dict['commandLineArgumentSeparator'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JobDefinition:
        """Create an instance of JobDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return JobDefinition.parse_obj(obj)

        _obj = JobDefinition.parse_obj({
            "job_id": ResourceId.from_dict(obj.get("jobId")) if obj.get("jobId") is not None else None,
            "name": obj.get("name"),
            "author": obj.get("author"),
            "date_created": obj.get("dateCreated"),
            "description": obj.get("description"),
            "docker_image": obj.get("dockerImage"),
            "ttl": obj.get("ttl"),
            "min_cpu": obj.get("minCpu"),
            "max_cpu": obj.get("maxCpu"),
            "min_memory": obj.get("minMemory"),
            "max_memory": obj.get("maxMemory"),
            "argument_definitions": dict(
                (_k, ArgumentDefinition.from_dict(_v))
                for _k, _v in obj.get("argumentDefinitions").items()
            )
            if obj.get("argumentDefinitions") is not None
            else None,
            "command_line_argument_separator": obj.get("commandLineArgumentSeparator"),
            "required_resources": RequiredResources.from_dict(obj.get("requiredResources")) if obj.get("requiredResources") is not None else None
        })
        return _obj
