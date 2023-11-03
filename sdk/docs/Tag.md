# Tag

Represents data of an image's tag

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the tag | [optional] 
**pull_time** | **datetime** | The latest pull time | [optional] 
**push_time** | **datetime** | The date of the tag&#39;s push | [optional] 
**signed** | **bool** | Indicates whether the tag is signed | [optional] 
**immutable** | **bool** | Indicates whether the tag is immutable | [optional] 

## Example

```python
from lusid_scheduler.models.tag import Tag

# TODO update the JSON string below
json = "{}"
# create an instance of Tag from a JSON string
tag_instance = Tag.from_json(json)
# print the JSON string representation of the object
print Tag.to_json()

# convert the object into a dict
tag_dict = tag_instance.to_dict()
# create an instance of Tag from a dict
tag_form_dict = tag.from_dict(tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


