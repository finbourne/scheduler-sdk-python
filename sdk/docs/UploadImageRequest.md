# UploadImageRequest

Request to upload image for Scheduler use
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_name** | **str** | Name of the image to be uploaded | 
## Example

```python
from lusid_scheduler.models.upload_image_request import UploadImageRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

image_name: StrictStr = "example_image_name"
upload_image_request_instance = UploadImageRequest(image_name=image_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

