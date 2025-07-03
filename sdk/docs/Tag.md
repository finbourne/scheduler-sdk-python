# Tag

Represents data of an image's tag
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the tag | [optional] 
**pull_time** | **datetime** | The latest pull time | [optional] 
**push_time** | **datetime** | The date of the tag&#39;s push | [optional] 
**signed** | **bool** | Indicates whether the tag is signed | [optional] 
**immutable** | **bool** | Indicates whether the tag is immutable | [optional] 
## Example

```python
from lusid_scheduler.models.tag import Tag
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr
from datetime import datetime
name: Optional[StrictStr] = "example_name"
pull_time: Optional[datetime] = # Replace with your value
push_time: Optional[datetime] = # Replace with your value
signed: Optional[StrictBool] = # Replace with your value
signed:Optional[StrictBool] = None
immutable: Optional[StrictBool] = # Replace with your value
immutable:Optional[StrictBool] = None
tag_instance = Tag(name=name, pull_time=pull_time, push_time=push_time, signed=signed, immutable=immutable)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

