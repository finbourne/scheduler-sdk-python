# ScheduleDefinition

Schedule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_identifier** | [**ResourceId**](ResourceId.md) |  | 
**job_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**name** | **str** | A display name for this Schedule | [optional] 
**description** | **str** | A description of the Schedule | [optional] 
**author** | **str** | Name of the author of this schedule | [optional] 
**owner** | **str** | Name of owner of this schedule | [optional] 
**use_as_auth** | **str** | User to runs schedule when automatically run and authenticates   requests in the schedule | [optional] 
**arguments** | **Dict[str, str]** | All arguments specified by this Schedule that will be passed in to the Job | [optional] 
**trigger** | [**Trigger**](Trigger.md) |  | [optional] 
**notifications** | [**List[Notification]**](Notification.md) | Notifications for this Schedule | [optional] 
**enabled** | **bool** | The status of this schedule | [optional] 

## Example

```python
from finbourne_scheduler.models.schedule_definition import ScheduleDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleDefinition from a JSON string
schedule_definition_instance = ScheduleDefinition.from_json(json)
# print the JSON string representation of the object
print ScheduleDefinition.to_json()

# convert the object into a dict
schedule_definition_dict = schedule_definition_instance.to_dict()
# create an instance of ScheduleDefinition from a dict
schedule_definition_form_dict = schedule_definition.from_dict(schedule_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


