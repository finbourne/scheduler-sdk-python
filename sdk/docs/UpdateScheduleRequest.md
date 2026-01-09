# UpdateScheduleRequest

Create a schedule definition
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** | The updated name of the schedule | 
**description** | **str** | The updated description of the schedule | 
**author** | **str** | The updated author of the schedule | [optional] 
**owner** | **str** | The update owner of the schedule | [optional] 
**arguments** | **Dict[str, Optional[str]]** | Updated arguments to be passed to the job Note: The new arguments will completely replace old arguments | [optional] 
**trigger** | [**Trigger**](Trigger.md) |  | [optional] 
**notifications** | [**List[Notification]**](Notification.md) | Updated notifications for this schedule | [optional] 
**enabled** | **bool** | Specify whether schedule is enabled or not Defaults to true | [optional] 
**use_as_auth** | **str** | Id of user associated with schedule. All calls to FINBOURNE services as part of execution of this schedule will be authenticated as this  user. Can be null, in which case we&#39;ll default to that of the user  making this request | [optional] 
## Example

```python
from lusid_scheduler.models.update_schedule_request import UpdateScheduleRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

job_id: ResourceId = # Replace with your value
name: StrictStr = "example_name"
description: StrictStr = "example_description"
author: Optional[StrictStr] = "example_author"
owner: Optional[StrictStr] = "example_owner"
arguments: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
trigger: Optional[Trigger] = None
notifications: Optional[List[Notification]] = # Replace with your value
enabled: Optional[StrictBool] = # Replace with your value
enabled:Optional[StrictBool] = None
use_as_auth: Optional[StrictStr] = "example_use_as_auth"
update_schedule_request_instance = UpdateScheduleRequest(job_id=job_id, name=name, description=description, author=author, owner=owner, arguments=arguments, trigger=trigger, notifications=notifications, enabled=enabled, use_as_auth=use_as_auth)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

