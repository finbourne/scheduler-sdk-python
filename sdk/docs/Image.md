# Image

Represents the metadata of an image
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the image | [optional] 
**push_time** | **datetime** | The push time of the image | [optional] 
**pull_time** | **datetime** | The latest pull time of the image | [optional] 
**digest** | **str** | The digest of the image | [optional] 
**size** | **int** | The size of the image (in bytes) | [optional] 
**tags** | [**List[Tag]**](Tag.md) | The tags of the image | [optional] 
**scan_report** | [**ScanReport**](ScanReport.md) |  | [optional] 
## Example

```python
from lusid_scheduler.models.image import Image
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist
from datetime import datetime
name: Optional[StrictStr] = "example_name"
push_time: Optional[datetime] = # Replace with your value
pull_time: Optional[datetime] = # Replace with your value
digest: Optional[StrictStr] = "example_digest"
size: Optional[StrictInt] = # Replace with your value
tags: Optional[conlist(Tag)] = # Replace with your value
scan_report: Optional[ScanReport] = # Replace with your value
image_instance = Image(name=name, push_time=push_time, pull_time=pull_time, digest=digest, size=size, tags=tags, scan_report=scan_report)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

