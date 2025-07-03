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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

lusid_apis: Optional[conlist(StrictStr)] = # Replace with your value
lusid_file_system: Optional[conlist(StrictStr)] = # Replace with your value
external_calls: Optional[conlist(StrictStr)] = # Replace with your value
required_resources_instance = RequiredResources(lusid_apis=lusid_apis, lusid_file_system=lusid_file_system, external_calls=external_calls)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

