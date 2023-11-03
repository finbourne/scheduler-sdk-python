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

# TODO update the JSON string below
json = "{}"
# create an instance of ScanSummary from a JSON string
scan_summary_instance = ScanSummary.from_json(json)
# print the JSON string representation of the object
print ScanSummary.to_json()

# convert the object into a dict
scan_summary_dict = scan_summary_instance.to_dict()
# create an instance of ScanSummary from a dict
scan_summary_form_dict = scan_summary.from_dict(scan_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


