# Repository

An object representation of a repository
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The identifier of the repository | [optional] 
**creation_time** | **datetime** | Date of  repository creation | [optional] 
**last_update** | **datetime** | The last update of the repository | [optional] 
**description** | **str** | Description of the repository | [optional] 
**pull_count** | **int** | Number of times images were pulled from this repository | [optional] 
**image_count** | **int** | The number of versions of this image | [optional] 
**images** | [**Link**](Link.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid_scheduler.models.repository import Repository
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist
from datetime import datetime
name: Optional[StrictStr] = "example_name"
creation_time: Optional[datetime] = # Replace with your value
last_update: Optional[datetime] = # Replace with your value
description: Optional[StrictStr] = "example_description"
pull_count: Optional[StrictInt] = # Replace with your value
image_count: Optional[StrictInt] = # Replace with your value
images: Optional[Link] = None
links: Optional[conlist(Link)] = None
repository_instance = Repository(name=name, creation_time=creation_time, last_update=last_update, description=description, pull_count=pull_count, image_count=image_count, images=images, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

