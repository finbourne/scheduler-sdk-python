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
from finbourne_scheduler.models.required_resources import RequiredResources

# TODO update the JSON string below
json = "{}"
# create an instance of RequiredResources from a JSON string
required_resources_instance = RequiredResources.from_json(json)
# print the JSON string representation of the object
print RequiredResources.to_json()

# convert the object into a dict
required_resources_dict = required_resources_instance.to_dict()
# create an instance of RequiredResources from a dict
required_resources_form_dict = required_resources.from_dict(required_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


