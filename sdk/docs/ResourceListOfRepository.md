# ResourceListOfRepository


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[Repository]**](Repository.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid_scheduler.models.resource_list_of_repository import ResourceListOfRepository

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfRepository from a JSON string
resource_list_of_repository_instance = ResourceListOfRepository.from_json(json)
# print the JSON string representation of the object
print ResourceListOfRepository.to_json()

# convert the object into a dict
resource_list_of_repository_dict = resource_list_of_repository_instance.to_dict()
# create an instance of ResourceListOfRepository from a dict
resource_list_of_repository_form_dict = resource_list_of_repository.from_dict(resource_list_of_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


