# ResourceListOfJobHistory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[JobHistory]**](JobHistory.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid_scheduler.models.resource_list_of_job_history import ResourceListOfJobHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfJobHistory from a JSON string
resource_list_of_job_history_instance = ResourceListOfJobHistory.from_json(json)
# print the JSON string representation of the object
print ResourceListOfJobHistory.to_json()

# convert the object into a dict
resource_list_of_job_history_dict = resource_list_of_job_history_instance.to_dict()
# create an instance of ResourceListOfJobHistory from a dict
resource_list_of_job_history_form_dict = resource_list_of_job_history.from_dict(resource_list_of_job_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


