# ImageSummary

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
**scan_status** | **str** | The Scan Status of the stated image | [optional] 
**scan_summary** | [**ScanSummary**](ScanSummary.md) |  | [optional] 
**link** | [**Link**](Link.md) |  | [optional] 
## Example

```python
from lusid_scheduler.models.image_summary import ImageSummary
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist
from datetime import datetime
name: Optional[StrictStr] = "example_name"
push_time: Optional[datetime] = # Replace with your value
pull_time: Optional[datetime] = # Replace with your value
digest: Optional[StrictStr] = "example_digest"
size: Optional[StrictInt] = # Replace with your value
tags: Optional[conlist(Tag)] = # Replace with your value
scan_status: Optional[StrictStr] = "example_scan_status"
scan_summary: Optional[ScanSummary] = # Replace with your value
link: Optional[Link] = None
image_summary_instance = ImageSummary(name=name, push_time=push_time, pull_time=pull_time, digest=digest, size=size, tags=tags, scan_status=scan_status, scan_summary=scan_summary, link=link)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

