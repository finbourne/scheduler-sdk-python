# ImageSummary

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
**scan_status** | **str** | The Scan Status of the stated image | [optional] 
**scan_summary** | [**ScanSummary**](ScanSummary.md) |  | [optional] 
**link** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from finbourne_scheduler.models.image_summary import ImageSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ImageSummary from a JSON string
image_summary_instance = ImageSummary.from_json(json)
# print the JSON string representation of the object
print ImageSummary.to_json()

# convert the object into a dict
image_summary_dict = image_summary_instance.to_dict()
# create an instance of ImageSummary from a dict
image_summary_form_dict = image_summary.from_dict(image_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


