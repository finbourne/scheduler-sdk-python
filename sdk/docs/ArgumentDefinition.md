# ArgumentDefinition

Job argument definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** | Data type of the argument | 
**required** | **bool** | Optionality of the argument | [optional] 
**description** | **str** | Argument description | 
**order** | **int** | The order of the argument | 
**constraints** | **str** | Constrains of the argument value | [optional] 
**passed_as** | **str** | Specifies how this argument should be passed in  Allowed values are: CommandLine or EnvironmentVariable    Defaults to: CommandLine | 
**default_value** | **str** | Specify a default value for this argument if no value is provided  The value needs to be convertible to the associated data type | [optional] 

## Example

```python
from lusid_scheduler.models.argument_definition import ArgumentDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of ArgumentDefinition from a JSON string
argument_definition_instance = ArgumentDefinition.from_json(json)
# print the JSON string representation of the object
print ArgumentDefinition.to_json()

# convert the object into a dict
argument_definition_dict = argument_definition_instance.to_dict()
# create an instance of ArgumentDefinition from a dict
argument_definition_form_dict = argument_definition.from_dict(argument_definition_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


