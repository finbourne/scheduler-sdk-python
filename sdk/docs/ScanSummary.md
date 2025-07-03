# ScanSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixable** | **int** | The number of vulnerabilities that have a known fix | [optional] 
**total** | **int** | The total number of vulnerabilities | [optional] 
**critical** | **int** | The number of Critical severity vulnerabilities | [optional] 
**high** | **int** | The number of High severity vulnerabilities | [optional] 
**medium** | **int** | The number of Medium severity vulnerabilities | [optional] 
**low** | **int** | The number of Low severity vulnerabilities | [optional] 
**negligible** | **int** | The number of Negligible severity vulnerabilities | [optional] 
**unknown** | **int** | The number of Unknown severity vulnerabilities | [optional] 
## Example

```python
from lusid_scheduler.models.scan_summary import ScanSummary
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictInt

fixable: Optional[StrictInt] = # Replace with your value
fixable: Optional[StrictInt] = None
total: Optional[StrictInt] = # Replace with your value
total: Optional[StrictInt] = None
critical: Optional[StrictInt] = # Replace with your value
critical: Optional[StrictInt] = None
high: Optional[StrictInt] = # Replace with your value
high: Optional[StrictInt] = None
medium: Optional[StrictInt] = # Replace with your value
medium: Optional[StrictInt] = None
low: Optional[StrictInt] = # Replace with your value
low: Optional[StrictInt] = None
negligible: Optional[StrictInt] = # Replace with your value
negligible: Optional[StrictInt] = None
unknown: Optional[StrictInt] = # Replace with your value
unknown: Optional[StrictInt] = None
scan_summary_instance = ScanSummary(fixable=fixable, total=total, critical=critical, high=high, medium=medium, low=low, negligible=negligible, unknown=unknown)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

