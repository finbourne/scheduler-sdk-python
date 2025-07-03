# ScheduleDefinition

Schedule
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_identifier** | [**ResourceId**](ResourceId.md) |  | 
**job_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**name** | **str** | A display name for this Schedule | [optional] 
**description** | **str** | A description of the Schedule | [optional] 
**author** | **str** | Name of the author of this schedule | [optional] 
**owner** | **str** | Name of owner of this schedule | [optional] 
**use_as_auth** | **str** | User to runs schedule when automatically run and authenticates   requests in the schedule | [optional] 
**arguments** | **Dict[str, str]** | All arguments specified by this Schedule that will be passed in to the Job | [optional] 
**trigger** | [**Trigger**](Trigger.md) |  | [optional] 
**notifications** | [**List[Notification]**](Notification.md) | Notifications for this Schedule | [optional] 
**enabled** | **bool** | The status of this schedule | [optional] 
## Example

```python
from lusid_scheduler.models.schedule_definition import ScheduleDefinition
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist

schedule_identifier: ResourceId = # Replace with your value
job_id: Optional[ResourceId] = # Replace with your value
name: Optional[StrictStr] = "example_name"
description: Optional[StrictStr] = "example_description"
author: Optional[StrictStr] = "example_author"
owner: Optional[StrictStr] = "example_owner"
use_as_auth: Optional[StrictStr] = "example_use_as_auth"
arguments: Optional[Dict[str, StrictStr]] = # Replace with your value
trigger: Optional[Trigger] = None
notifications: Optional[conlist(Notification)] = # Replace with your value
enabled: Optional[StrictBool] = # Replace with your value
enabled:Optional[StrictBool] = None
schedule_definition_instance = ScheduleDefinition(schedule_identifier=schedule_identifier, job_id=job_id, name=name, description=description, author=author, owner=owner, use_as_auth=use_as_auth, arguments=arguments, trigger=trigger, notifications=notifications, enabled=enabled)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

