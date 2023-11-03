# Trigger

Holds different kinds of triggers  A schedule may only have one type of trigger

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_trigger** | [**TimeTrigger**](TimeTrigger.md) |  | [optional] 

## Example

```python
from lusid_scheduler.models.trigger import Trigger

# TODO update the JSON string below
json = "{}"
# create an instance of Trigger from a JSON string
trigger_instance = Trigger.from_json(json)
# print the JSON string representation of the object
print Trigger.to_json()

# convert the object into a dict
trigger_dict = trigger_instance.to_dict()
# create an instance of Trigger from a dict
trigger_form_dict = trigger.from_dict(trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


