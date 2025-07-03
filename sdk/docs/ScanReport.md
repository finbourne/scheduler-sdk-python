# ScanReport

Represents the details of a security scan of an image
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**severity** | **str** | The overall severity. For example : \&quot;High\&quot; or \&quot;None\&quot; | [optional] 
**status** | **str** | The status of the report | [optional] 
**start_time** | **datetime** | The start time of the scanning process | [optional] 
**end_time** | **datetime** | The end time of the scanning process | [optional] 
**scan_duration** | **int** | The duration of the scan in seconds | [optional] 
**summary** | [**ScanSummary**](ScanSummary.md) |  | [optional] 
**vulnerabilities** | [**List[Vulnerability]**](Vulnerability.md) | List of Finbourne.Scheduler.WebApi.Dtos.Images.Vulnerability | [optional] 
## Example

```python
from lusid_scheduler.models.scan_report import ScanReport
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist
from datetime import datetime
severity: Optional[StrictStr] = "example_severity"
status: Optional[StrictStr] = "example_status"
start_time: Optional[datetime] = # Replace with your value
end_time: Optional[datetime] = # Replace with your value
scan_duration: Optional[StrictInt] = # Replace with your value
scan_duration: Optional[StrictInt] = None
summary: Optional[ScanSummary] = None
vulnerabilities: Optional[conlist(Vulnerability)] = # Replace with your value
scan_report_instance = ScanReport(severity=severity, status=status, start_time=start_time, end_time=end_time, scan_duration=scan_duration, summary=summary, vulnerabilities=vulnerabilities)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

