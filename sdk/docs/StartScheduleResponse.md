# StartScheduleResponse

Response from a manual run of a schedule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**job_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**run_id** | **str** | Unique RunId of the started schedule | [optional] 
**status** | **str** | Status of the started schedule | [optional] 
**result** | **str** | Link to the result of the job run when completed | [optional] 

## Example

```python
from finbourne_scheduler.models.start_schedule_response import StartScheduleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StartScheduleResponse from a JSON string
start_schedule_response_instance = StartScheduleResponse.from_json(json)
# print the JSON string representation of the object
print StartScheduleResponse.to_json()

# convert the object into a dict
start_schedule_response_dict = start_schedule_response_instance.to_dict()
# create an instance of StartScheduleResponse from a dict
start_schedule_response_form_dict = start_schedule_response.from_dict(start_schedule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


