# JobDefinition

Definition of a job

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** | Name of the job | [optional] 
**author** | **str** | Author of the job | [optional] 
**date_created** | **datetime** | Date when job was created | [optional] 
**description** | **str** | Description of this job | [optional] 
**docker_image** | **str** | Information about the docker image in the format “image_source/image_name:image_tag” | [optional] 
**ttl** | **int** | Time To Live of the job run in seconds  Defaults to 5 minutes(300) | [optional] 
**min_cpu** | **str** | Specifies  minimum number of CPUs to be allocated for the job  Default to 2 | [optional] 
**max_cpu** | **str** | Specifies  maximum number of CPUs to be allocated for the job | [optional] 
**min_memory** | **str** | Specifies the minimum amount of memory (in GiB) to be allocated for the job | [optional] 
**max_memory** | **str** | Specifies the maximum amount of memory (in GiB) to be allocated for the job | [optional] 
**argument_definitions** | [**Dict[str, ArgumentDefinition]**](ArgumentDefinition.md) | All arguments for this job to run | [optional] 
**command_line_argument_separator** | **str** | Value to separate command line arguments  e.g : If a job has a command line argument named &#39;folder&#39; and the runtime value is &#39;s3://path&#39; then this  would be supplied to the command as &#39;folder{separatorValue}s3://path&#39;  Default to a space | [optional] 
**required_resources** | [**RequiredResources**](RequiredResources.md) |  | 

## Example

```python
from finbourne_scheduler.models.job_definition import JobDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of JobDefinition from a JSON string
job_definition_instance = JobDefinition.from_json(json)
# print the JSON string representation of the object
print JobDefinition.to_json()

# convert the object into a dict
job_definition_dict = job_definition_instance.to_dict()
# create an instance of JobDefinition from a dict
job_definition_form_dict = job_definition.from_dict(job_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


