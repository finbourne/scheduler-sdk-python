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

# TODO update the JSON string below
json = "{}"
# create an instance of ScanReport from a JSON string
scan_report_instance = ScanReport.from_json(json)
# print the JSON string representation of the object
print ScanReport.to_json()

# convert the object into a dict
scan_report_dict = scan_report_instance.to_dict()
# create an instance of ScanReport from a dict
scan_report_form_dict = scan_report.from_dict(scan_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


