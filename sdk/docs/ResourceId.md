# ResourceId

Resource Id
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | Scope of the resource | 
**code** | **str** | Code of the resource | 
## Example

```python
from lusid_scheduler.models.resource_id import ResourceId
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
resource_id_instance = ResourceId(scope=scope, code=code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

