# RequiredResources

Information related to a jobs required access to resources
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lusid_apis** | **List[str]** | List of LUSID APIs the job needs access to | [optional] 
**lusid_file_system** | **List[str]** | List of S3 bucket or folder names that the job can access | [optional] 
**external_calls** | **List[str]** | External URLs that the job can call | [optional] 
## Example

```python
from lusid_scheduler.models.required_resources import RequiredResources
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

lusid_apis: Optional[List[StrictStr]] = # Replace with your value
lusid_file_system: Optional[List[StrictStr]] = # Replace with your value
external_calls: Optional[List[StrictStr]] = # Replace with your value
required_resources_instance = RequiredResources(lusid_apis=lusid_apis, lusid_file_system=lusid_file_system, external_calls=external_calls)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

