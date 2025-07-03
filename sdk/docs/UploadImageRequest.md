# UploadImageRequest

Request to upload image for Scheduler use
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_name** | **str** | Name of the image to be uploaded | 
## Example

```python
from lusid_scheduler.models.upload_image_request import UploadImageRequest
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

image_name: StrictStr = "example_image_name"
upload_image_request_instance = UploadImageRequest(image_name=image_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

