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
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictInt, StrictStr, constr

data_type: StrictStr = "example_data_type"
required: Optional[StrictBool] = # Replace with your value
required:Optional[StrictBool] = None
description: StrictStr = "example_description"
order: StrictInt = # Replace with your value
order: StrictInt = 42
constraints: Optional[StrictStr] = "example_constraints"
passed_as: StrictStr = "example_passed_as"
default_value: Optional[StrictStr] = "example_default_value"
argument_definition_instance = ArgumentDefinition(data_type=data_type, required=required, description=description, order=order, constraints=constraints, passed_as=passed_as, default_value=default_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

