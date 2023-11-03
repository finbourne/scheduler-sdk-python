# StartJobRequest

Job start definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | **Dict[str, str]** | All arguments needed for the Job to run | [optional] 
**notifications** | [**List[Notification]**](Notification.md) | Notifications for this Job | [optional] 
**use_as_auth** | **str** | Id of user associated with schedule. All calls to FINBOURNE services  as part of execution of this schedule will be authenticated as this   user. Can be null, in which case we&#39;ll default to that of the user   making this request | [optional] 

## Example

```python
from lusid_scheduler.models.start_job_request import StartJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartJobRequest from a JSON string
start_job_request_instance = StartJobRequest.from_json(json)
# print the JSON string representation of the object
print StartJobRequest.to_json()

# convert the object into a dict
start_job_request_dict = start_job_request_instance.to_dict()
# create an instance of StartJobRequest from a dict
start_job_request_form_dict = start_job_request.from_dict(start_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


