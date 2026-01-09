# Notification

Notification type
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fire_on** | **str** | Condition for the notification | [optional] [readonly] 
**transport** | **str** | The type of the notification | [optional] 
**destination** | **List[str]** | Where the notification should be sent | [optional] 
## Example

```python
from lusid_scheduler.models.notification import Notification
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fire_on: Optional[StrictStr] = "example_fire_on"
transport: Optional[StrictStr] = "example_transport"
destination: Optional[List[StrictStr]] = # Replace with your value
notification_instance = Notification(fire_on=fire_on, transport=transport, destination=destination)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

