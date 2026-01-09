# TimeTrigger

Time-based trigger
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** | Cron expression | [optional] 
**time_zone** | **str** | Time zone of the Cron expression. If not provided, defaults to UTC | [optional] 
## Example

```python
from lusid_scheduler.models.time_trigger import TimeTrigger
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

expression: Optional[StrictStr] = "example_expression"
time_zone: Optional[StrictStr] = "example_time_zone"
time_trigger_instance = TimeTrigger(expression=expression, time_zone=time_zone)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

