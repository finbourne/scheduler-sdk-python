# UploadImageInstructions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**docker_login_command** | **str** |  | 
**build_versioned_docker_image_command** | **str** |  | 
**tag_versioned_docker_image_command** | **str** |  | 
**push_versioned_docker_image_command** | **str** |  | 
**tag_latest_docker_image_command** | **str** |  | [optional] 
**push_latest_docker_image_command** | **str** |  | [optional] 
**expiry_time** | **datetime** |  | [optional] 
## Example

```python
from lusid_scheduler.models.upload_image_instructions import UploadImageInstructions
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr
from datetime import datetime
docker_login_command: StrictStr = "example_docker_login_command"
build_versioned_docker_image_command: StrictStr = "example_build_versioned_docker_image_command"
tag_versioned_docker_image_command: StrictStr = "example_tag_versioned_docker_image_command"
push_versioned_docker_image_command: StrictStr = "example_push_versioned_docker_image_command"
tag_latest_docker_image_command: Optional[StrictStr] = "example_tag_latest_docker_image_command"
push_latest_docker_image_command: Optional[StrictStr] = "example_push_latest_docker_image_command"
expiry_time: Optional[datetime] = # Replace with your value
upload_image_instructions_instance = UploadImageInstructions(docker_login_command=docker_login_command, build_versioned_docker_image_command=build_versioned_docker_image_command, tag_versioned_docker_image_command=tag_versioned_docker_image_command, push_versioned_docker_image_command=push_versioned_docker_image_command, tag_latest_docker_image_command=tag_latest_docker_image_command, push_latest_docker_image_command=push_latest_docker_image_command, expiry_time=expiry_time)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

