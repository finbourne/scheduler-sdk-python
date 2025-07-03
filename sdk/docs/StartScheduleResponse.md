# StartScheduleResponse

Response from a manual run of a schedule
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**job_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**run_id** | **str** | Unique RunId of the started schedule | [optional] 
**status** | **str** | Status of the started schedule | [optional] 
**result** | **str** | Link to the result of the job run when completed | [optional] 
## Example

```python
from lusid_scheduler.models.start_schedule_response import StartScheduleResponse
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

schedule_id: Optional[ResourceId] = # Replace with your value
job_id: Optional[ResourceId] = # Replace with your value
run_id: Optional[StrictStr] = "example_run_id"
status: Optional[StrictStr] = "example_status"
result: Optional[StrictStr] = "example_result"
start_schedule_response_instance = StartScheduleResponse(schedule_id=schedule_id, job_id=job_id, run_id=run_id, status=status, result=result)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

