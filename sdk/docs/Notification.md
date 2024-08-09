# Notification

Notification type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fire_on** | **str** | Condition for the notification | [optional] [readonly] 
**transport** | **str** | The type of the notification | [optional] 
**destination** | **List[str]** | Where the notification should be sent | [optional] 

## Example

```python
from lusid_scheduler.models.notification import Notification

# TODO update the JSON string below
json = "{}"
# create an instance of Notification from a JSON string
notification_instance = Notification.from_json(json)
# print the JSON string representation of the object
print Notification.to_json()

# convert the object into a dict
notification_dict = notification_instance.to_dict()
# create an instance of Notification from a dict
notification_form_dict = notification.from_dict(notification_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


