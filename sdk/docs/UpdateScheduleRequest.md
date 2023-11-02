# UpdateScheduleRequest

Create a schedule definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** | The updated name of the schedule | 
**description** | **str** | The updated description of the schedule | 
**author** | **str** | The updated author of the schedule | [optional] 
**owner** | **str** | The update owner of the schedule | [optional] 
**arguments** | **Dict[str, str]** | Updated arguments to be passed to the job  Note: The new arguments will completely replace old arguments | [optional] 
**trigger** | [**Trigger**](Trigger.md) |  | [optional] 
**notifications** | [**List[Notification]**](Notification.md) | Updated notifications for this schedule | 
**enabled** | **bool** | Specify whether schedule is enabled or not  Defaults to true | [optional] 
**use_as_auth** | **str** | Id of user associated with schedule. All calls to FINBOURNE services  as part of execution of this schedule will be authenticated as this   user. Can be null, in which case we&#39;ll default to that of the user   making this request | [optional] 

## Example

```python
from finbourne_scheduler.models.update_schedule_request import UpdateScheduleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateScheduleRequest from a JSON string
update_schedule_request_instance = UpdateScheduleRequest.from_json(json)
# print the JSON string representation of the object
print UpdateScheduleRequest.to_json()

# convert the object into a dict
update_schedule_request_dict = update_schedule_request_instance.to_dict()
# create an instance of UpdateScheduleRequest from a dict
update_schedule_request_form_dict = update_schedule_request.from_dict(update_schedule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


