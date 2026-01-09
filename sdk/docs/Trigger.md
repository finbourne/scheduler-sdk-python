# Trigger

Holds different kinds of triggers A schedule may only have one type of trigger
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_trigger** | [**TimeTrigger**](TimeTrigger.md) |  | [optional] 
## Example

```python
from lusid_scheduler.models.trigger import Trigger
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

time_trigger: Optional[TimeTrigger] = # Replace with your value
trigger_instance = Trigger(time_trigger=time_trigger)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

