# TimeTrigger

Time-based trigger

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** | Cron expression | [optional] 
**time_zone** | **str** | Time zone of the Cron expression. If not provided, defaults to UTC | [optional] 

## Example

```python
from lusid_scheduler.models.time_trigger import TimeTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrigger from a JSON string
time_trigger_instance = TimeTrigger.from_json(json)
# print the JSON string representation of the object
print TimeTrigger.to_json()

# convert the object into a dict
time_trigger_dict = time_trigger_instance.to_dict()
# create an instance of TimeTrigger from a dict
time_trigger_form_dict = time_trigger.from_dict(time_trigger_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


