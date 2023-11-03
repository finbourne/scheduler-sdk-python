# Image

Represents the metadata of an image

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the image | [optional] 
**push_time** | **datetime** | The push time of the image | [optional] 
**pull_time** | **datetime** | The latest pull time of the image | [optional] 
**digest** | **str** | The digest of the image | [optional] 
**size** | **int** | The size of the image (in bytes) | [optional] 
**tags** | [**List[Tag]**](Tag.md) | The tags of the image | [optional] 
**scan_report** | [**ScanReport**](ScanReport.md) |  | [optional] 

## Example

```python
from lusid_scheduler.models.image import Image

# TODO update the JSON string below
json = "{}"
# create an instance of Image from a JSON string
image_instance = Image.from_json(json)
# print the JSON string representation of the object
print Image.to_json()

# convert the object into a dict
image_dict = image_instance.to_dict()
# create an instance of Image from a dict
image_form_dict = image.from_dict(image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


