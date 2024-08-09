# UploadImageRequest

Request to upload image for Scheduler use

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_name** | **str** | Name of the image to be uploaded | 

## Example

```python
from lusid_scheduler.models.upload_image_request import UploadImageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UploadImageRequest from a JSON string
upload_image_request_instance = UploadImageRequest.from_json(json)
# print the JSON string representation of the object
print UploadImageRequest.to_json()

# convert the object into a dict
upload_image_request_dict = upload_image_request_instance.to_dict()
# create an instance of UploadImageRequest from a dict
upload_image_request_form_dict = upload_image_request.from_dict(upload_image_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


