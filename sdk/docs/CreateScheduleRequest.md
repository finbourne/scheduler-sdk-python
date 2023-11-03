# CreateScheduleRequest

Create a schedule definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_id** | [**ResourceId**](ResourceId.md) |  | 
**job_id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** | A display name for this Schedule | 
**description** | **str** | A description of the Schedule | 
**author** | **str** | Name of the author of this schedule | [optional] 
**owner** | **str** | Name of owner of this schedule | [optional] 
**arguments** | **Dict[str, str]** | All arguments specified by this Schedule that will be passed in to the Job | [optional] 
**trigger** | [**Trigger**](Trigger.md) |  | [optional] 
**notifications** | [**List[Notification]**](Notification.md) | Notifications for this Schedule | 
**enabled** | **bool** | Specify whether schedule is enabled or not  Defaults to true | [optional] 
**use_as_auth** | **str** | Id of user associated with schedule. All calls to FINBOURNE services  as part of execution of this schedule will be authenticated as this   user. Can be null, in which case we&#39;ll default to that of the user   making this request | [optional] 

## Example

```python
from lusid_scheduler.models.create_schedule_request import CreateScheduleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScheduleRequest from a JSON string
create_schedule_request_instance = CreateScheduleRequest.from_json(json)
# print the JSON string representation of the object
print CreateScheduleRequest.to_json()

# convert the object into a dict
create_schedule_request_dict = create_schedule_request_instance.to_dict()
# create an instance of CreateScheduleRequest from a dict
create_schedule_request_form_dict = create_schedule_request.from_dict(create_schedule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


