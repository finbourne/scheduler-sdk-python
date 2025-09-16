# CreateScheduleRequest

Create a schedule definition
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_id** | [**ResourceId**](ResourceId.md) |  | 
**job_id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** | A display name for this Schedule | 
**description** | **str** | A description of the Schedule | 
**author** | **str** | Name of the author of this schedule | [optional] 
**owner** | **str** | Name of owner of this schedule | [optional] 
**arguments** | **Dict[str, str]** | All arguments specified by this Schedule that will be passed in to the Job | [optional] 
**trigger** | [**Trigger**](Trigger.md) |  | [optional] 
**notifications** | [**List[Notification]**](Notification.md) | Notifications for this Schedule | [optional] 
**enabled** | **bool** | Specify whether schedule is enabled or not Defaults to true | [optional] 
**use_as_auth** | **str** | Id of user associated with schedule. All calls to FINBOURNE services as part of execution of this schedule will be authenticated as this  user. Can be null, in which case we&#39;ll default to that of the user  making this request | [optional] 
## Example

```python
from lusid_scheduler.models.create_schedule_request import CreateScheduleRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist, constr, validator

schedule_id: ResourceId = # Replace with your value
job_id: ResourceId = # Replace with your value
name: StrictStr = "example_name"
description: StrictStr = "example_description"
author: Optional[StrictStr] = "example_author"
owner: Optional[StrictStr] = "example_owner"
arguments: Optional[Dict[str, StrictStr]] = # Replace with your value
trigger: Optional[Trigger] = None
notifications: Optional[conlist(Notification)] = # Replace with your value
enabled: Optional[StrictBool] = # Replace with your value
enabled:Optional[StrictBool] = None
use_as_auth: Optional[StrictStr] = "example_use_as_auth"
create_schedule_request_instance = CreateScheduleRequest(schedule_id=schedule_id, job_id=job_id, name=name, description=description, author=author, owner=owner, arguments=arguments, trigger=trigger, notifications=notifications, enabled=enabled, use_as_auth=use_as_auth)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

