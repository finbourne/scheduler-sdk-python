# ResourceListOfImageSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ImageSummary]**](ImageSummary.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid_scheduler.models.resource_list_of_image_summary import ResourceListOfImageSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfImageSummary from a JSON string
resource_list_of_image_summary_instance = ResourceListOfImageSummary.from_json(json)
# print the JSON string representation of the object
print ResourceListOfImageSummary.to_json()

# convert the object into a dict
resource_list_of_image_summary_dict = resource_list_of_image_summary_instance.to_dict()
# create an instance of ResourceListOfImageSummary from a dict
resource_list_of_image_summary_form_dict = resource_list_of_image_summary.from_dict(resource_list_of_image_summary_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


