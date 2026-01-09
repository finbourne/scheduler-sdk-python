# StartJobResponse

Response from starting a job
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**run_id** | **str** | Unique RunId of the started job run | [optional] 
**status** | **str** | Link to the status of the started job | [optional] 
**result** | **str** | Link to the result of the job run when completed | [optional] 
## Example

```python
from lusid_scheduler.models.start_job_response import StartJobResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

job_id: Optional[ResourceId] = # Replace with your value
run_id: Optional[StrictStr] = "example_run_id"
status: Optional[StrictStr] = "example_status"
result: Optional[StrictStr] = "example_result"
start_job_response_instance = StartJobResponse(job_id=job_id, run_id=run_id, status=status, result=result)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

