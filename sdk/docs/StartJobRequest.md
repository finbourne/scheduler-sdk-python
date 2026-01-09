# StartJobRequest

Job start definition
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | **Dict[str, Optional[str]]** | All arguments needed for the Job to run | [optional] 
**notifications** | [**List[Notification]**](Notification.md) | Notifications for this Job | [optional] 
**use_as_auth** | **str** | Id of user associated with schedule. All calls to FINBOURNE services as part of execution of this schedule will be authenticated as this  user. Can be null, in which case we&#39;ll default to that of the user  making this request | [optional] 
## Example

```python
from lusid_scheduler.models.start_job_request import StartJobRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

arguments: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
notifications: Optional[List[Notification]] = # Replace with your value
use_as_auth: Optional[StrictStr] = "example_use_as_auth"
start_job_request_instance = StartJobRequest(arguments=arguments, notifications=notifications, use_as_auth=use_as_auth)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

