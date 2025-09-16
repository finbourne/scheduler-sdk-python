# CreateJobRequest

Definition of a job
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** | Name of the job | 
**author** | **str** | Author of the job | [optional] 
**date_created** | **datetime** | Date when job was created. Defaults to now. | [optional] 
**description** | **str** | Description of this job | 
**image_name** | **str** | The name of the Docker image that contains this job | 
**image_tag** | **str** | The tag of the Docker image that contains this job | 
**ttl** | **int** | Time To Live of the job run in seconds Defaults to 5 minutes(300) | [optional] 
**min_cpu** | **str** | Specifies  minimum number of CPUs to be allocated for the job Default to 2 | [optional] 
**max_cpu** | **str** | Specifies  maximum number of CPUs to be allocated for the job | [optional] 
**min_memory** | **str** | Specifies the minimum amount of memory  to be allocated for the job | [optional] 
**max_memory** | **str** | Specifies the maximum amount of memory to be allocated for the job | [optional] 
**argument_definitions** | [**Dict[str, ArgumentDefinition]**](ArgumentDefinition.md) | All arguments for this job to run | 
**command_line_argument_separator** | **str** | Value to separate command line arguments e.g : If a job has a command line argument named &#39;folder&#39; and the runtime value is &#39;s3://path&#39; then this would be supplied to the command as &#39;folder{separatorValue}s3://path&#39; Default to a space | [optional] 
**required_resources** | [**RequiredResources**](RequiredResources.md) |  | [optional] 
## Example

```python
from lusid_scheduler.models.create_job_request import CreateJobRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conint, constr, validator
from datetime import datetime
job_id: ResourceId = # Replace with your value
name: StrictStr = "example_name"
author: Optional[StrictStr] = "example_author"
date_created: Optional[datetime] = # Replace with your value
description: StrictStr = "example_description"
image_name: StrictStr = "example_image_name"
image_tag: StrictStr = "example_image_tag"
ttl: Optional[conint(strict=True, le=18000, ge=0)] = Field(None, description="Time To Live of the job run in seconds Defaults to 5 minutes(300)")
ttl: Optional[StrictInt] = None
min_cpu: Optional[StrictStr] = "example_min_cpu"
max_cpu: Optional[StrictStr] = "example_max_cpu"
min_memory: Optional[StrictStr] = "example_min_memory"
max_memory: Optional[StrictStr] = "example_max_memory"
argument_definitions: Dict[str, ArgumentDefinition] = # Replace with your value
command_line_argument_separator: Optional[StrictStr] = "example_command_line_argument_separator"
required_resources: Optional[RequiredResources] = # Replace with your value
create_job_request_instance = CreateJobRequest(job_id=job_id, name=name, author=author, date_created=date_created, description=description, image_name=image_name, image_tag=image_tag, ttl=ttl, min_cpu=min_cpu, max_cpu=max_cpu, min_memory=min_memory, max_memory=max_memory, argument_definitions=argument_definitions, command_line_argument_separator=command_line_argument_separator, required_resources=required_resources)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

