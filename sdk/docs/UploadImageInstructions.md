# UploadImageInstructions



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**docker_login_command** | **str** |  | 
**build_versioned_docker_image_command** | **str** |  | 
**tag_versioned_docker_image_command** | **str** |  | 
**push_versioned_docker_image_command** | **str** |  | 
**tag_latest_docker_image_command** | **str** |  | [optional] 
**push_latest_docker_image_command** | **str** |  | [optional] 
**expiry_time** | **datetime** |  | [optional] 

## Example

```python
from finbourne_scheduler.models.upload_image_instructions import UploadImageInstructions

# TODO update the JSON string below
json = "{}"
# create an instance of UploadImageInstructions from a JSON string
upload_image_instructions_instance = UploadImageInstructions.from_json(json)
# print the JSON string representation of the object
print UploadImageInstructions.to_json()

# convert the object into a dict
upload_image_instructions_dict = upload_image_instructions_instance.to_dict()
# create an instance of UploadImageInstructions from a dict
upload_image_instructions_form_dict = upload_image_instructions.from_dict(upload_image_instructions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


