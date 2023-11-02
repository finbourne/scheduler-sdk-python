# Repository

An object representation of a repository

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The identifier of the repository | [optional] 
**creation_time** | **datetime** | Date of  repository creation | [optional] 
**last_update** | **datetime** | The last update of the repository | [optional] 
**description** | **str** | Description of the repository | [optional] 
**pull_count** | **int** | Number of times images were pulled from this repository | [optional] 
**image_count** | **int** | The number of versions of this image | [optional] 
**images** | [**Link**](Link.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from finbourne_scheduler.models.repository import Repository

# TODO update the JSON string below
json = "{}"
# create an instance of Repository from a JSON string
repository_instance = Repository.from_json(json)
# print the JSON string representation of the object
print Repository.to_json()

# convert the object into a dict
repository_dict = repository_instance.to_dict()
# create an instance of Repository from a dict
repository_form_dict = repository.from_dict(repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


