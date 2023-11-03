# StartJobResponse

Response from starting a job

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**run_id** | **str** | Unique RunId of the started job run | [optional] 
**status** | **str** | Link to the status of the started job | [optional] 
**result** | **str** | Link to the result of the job run when completed | [optional] 

## Example

```python
from lusid_scheduler.models.start_job_response import StartJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StartJobResponse from a JSON string
start_job_response_instance = StartJobResponse.from_json(json)
# print the JSON string representation of the object
print StartJobResponse.to_json()

# convert the object into a dict
start_job_response_dict = start_job_response_instance.to_dict()
# create an instance of StartJobResponse from a dict
start_job_response_form_dict = start_job_response.from_dict(start_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


