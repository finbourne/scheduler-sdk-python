# ResourceListOfJobDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[JobDefinition]**](JobDefinition.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from finbourne_scheduler.models.resource_list_of_job_definition import ResourceListOfJobDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfJobDefinition from a JSON string
resource_list_of_job_definition_instance = ResourceListOfJobDefinition.from_json(json)
# print the JSON string representation of the object
print ResourceListOfJobDefinition.to_json()

# convert the object into a dict
resource_list_of_job_definition_dict = resource_list_of_job_definition_instance.to_dict()
# create an instance of ResourceListOfJobDefinition from a dict
resource_list_of_job_definition_form_dict = resource_list_of_job_definition.from_dict(resource_list_of_job_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


