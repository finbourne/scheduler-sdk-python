# Trigger

Holds different kinds of triggers A schedule may only have one type of trigger
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_trigger** | [**TimeTrigger**](TimeTrigger.md) |  | [optional] 
## Example

```python
from lusid_scheduler.models.trigger import Trigger
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field

time_trigger: Optional[TimeTrigger] = # Replace with your value
trigger_instance = Trigger(time_trigger=time_trigger)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

