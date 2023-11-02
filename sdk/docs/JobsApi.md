# finbourne_scheduler.JobsApi

All URIs are relative to *https://fbn-ci.lusid.com/scheduler2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_job**](JobsApi.md#create_job) | **POST** /api/jobs | [EXPERIMENTAL] CreateJob: Create a new job
[**delete_job**](JobsApi.md#delete_job) | **DELETE** /api/jobs/{scope}/{code} | [EXPERIMENTAL] DeleteJob: Delete a job
[**get_history**](JobsApi.md#get_history) | **GET** /api/jobs/history | [EXPERIMENTAL] GetHistory: Get the history of job runs
[**get_job_console_output**](JobsApi.md#get_job_console_output) | **GET** /api/jobs/history/{runId}/console | [EXPERIMENTAL] GetJobConsoleOutput: Gets the console output of a specific job run
[**get_run_history**](JobsApi.md#get_run_history) | **GET** /api/jobs/history/{runId} | [EXPERIMENTAL] GetRunHistory: Get the history for a single job run
[**get_schedules_for_a_job**](JobsApi.md#get_schedules_for_a_job) | **GET** /api/jobs/{scope}/{code}/schedules | [EXPERIMENTAL] GetSchedulesForAJob: Get all the schedules for a single job
[**list_jobs**](JobsApi.md#list_jobs) | **GET** /api/jobs | [EXPERIMENTAL] ListJobs: List the available jobs
[**run_job**](JobsApi.md#run_job) | **POST** /api/jobs/{scope}/{code}/$run | [EXPERIMENTAL] RunJob: Run a job immediately
[**update_job**](JobsApi.md#update_job) | **PUT** /api/jobs/{scope}/{code} | [EXPERIMENTAL] UpdateJob: Update a JobDefinition


# **create_job**
> JobDefinition create_job(create_job_request)

[EXPERIMENTAL] CreateJob: Create a new job

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_scheduler
from finbourne_scheduler.rest import ApiException
from finbourne_scheduler.models.create_job_request import CreateJobRequest
from finbourne_scheduler.models.job_definition import JobDefinition
from pprint import pprint

from finbourne_scheduler import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the finbourne_scheduler ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-ci.lusid.com/scheduler2"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_scheduler.JobsApi)
    create_job_request = {"jobId":{"scope":"JobScope","code":"JobCode"},"name":"Data loader","author":"Job author","dateCreated":"2019-12-11T00:00:00.0000000+00:00","description":"Load EOD data","imageName":"alpine","imageTag":"latest","ttl":500,"minCpu":"2","maxCpu":"4","minMemory":"0.5Mi","maxMemory":"500Mi","argumentDefinitions":{"SECRET1":{"dataType":"SecureString","required":true,"description":"Database credentials","order":1,"constraints":"None","passedAs":"EnvironmentVariable"}},"commandLineArgumentSeparator":" ","requiredResources":{"lusidApis":["Shrine, IBOR"],"lusidFileSystem":[],"externalCalls":["AWS"]}} # CreateJobRequest | The request to create a new job

    try:
        # [EXPERIMENTAL] CreateJob: Create a new job
        api_response = await api_instance.create_job(create_job_request)
        print("The response of JobsApi->create_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->create_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_job_request** | [**CreateJobRequest**](CreateJobRequest.md)| The request to create a new job | 

### Return type

[**JobDefinition**](JobDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job**
> ResourceListOfScheduleDefinition delete_job(scope, code)

[EXPERIMENTAL] DeleteJob: Delete a job

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_scheduler
from finbourne_scheduler.rest import ApiException
from finbourne_scheduler.models.resource_list_of_schedule_definition import ResourceListOfScheduleDefinition
from pprint import pprint

from finbourne_scheduler import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the finbourne_scheduler ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-ci.lusid.com/scheduler2"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_scheduler.JobsApi)
    scope = 'scope_example' # str | The scope of the job
    code = 'code_example' # str | The code of the job

    try:
        # [EXPERIMENTAL] DeleteJob: Delete a job
        api_response = await api_instance.delete_job(scope, code)
        print("The response of JobsApi->delete_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->delete_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the job | 
 **code** | **str**| The code of the job | 

### Return type

[**ResourceListOfScheduleDefinition**](ResourceListOfScheduleDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_history**
> ResourceListOfJobHistory get_history(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

[EXPERIMENTAL] GetHistory: Get the history of job runs

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_scheduler
from finbourne_scheduler.rest import ApiException
from finbourne_scheduler.models.resource_list_of_job_history import ResourceListOfJobHistory
from pprint import pprint

from finbourne_scheduler import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the finbourne_scheduler ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-ci.lusid.com/scheduler2"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_scheduler.JobsApi)
    page = 'page_example' # str | The pagination token to use to continue listing instruments from a previous call to list instruments.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
    sort_by = ['sort_by_example'] # List[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
    start = 56 # int | This field is obsolete, the value of this field would not be considered. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified. Maximum is 5000. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. (optional)

    try:
        # [EXPERIMENTAL] GetHistory: Get the history of job runs
        api_response = await api_instance.get_history(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
        print("The response of JobsApi->get_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| The pagination token to use to continue listing instruments from a previous call to list instruments.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **sort_by** | [**List[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **start** | **int**| This field is obsolete, the value of this field would not be considered. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified. Maximum is 5000. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 

### Return type

[**ResourceListOfJobHistory**](ResourceListOfJobHistory.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_console_output**
> str get_job_console_output(run_id)

[EXPERIMENTAL] GetJobConsoleOutput: Gets the console output of a specific job run

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_scheduler
from finbourne_scheduler.rest import ApiException
from pprint import pprint

from finbourne_scheduler import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the finbourne_scheduler ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-ci.lusid.com/scheduler2"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_scheduler.JobsApi)
    run_id = 'run_id_example' # str | The RunId of the job run

    try:
        # [EXPERIMENTAL] GetJobConsoleOutput: Gets the console output of a specific job run
        api_response = await api_instance.get_job_console_output(run_id)
        print("The response of JobsApi->get_job_console_output:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job_console_output: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The RunId of the job run | 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_history**
> JobRunResult get_run_history(run_id)

[EXPERIMENTAL] GetRunHistory: Get the history for a single job run

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_scheduler
from finbourne_scheduler.rest import ApiException
from finbourne_scheduler.models.job_run_result import JobRunResult
from pprint import pprint

from finbourne_scheduler import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the finbourne_scheduler ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-ci.lusid.com/scheduler2"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_scheduler.JobsApi)
    run_id = 'run_id_example' # str | The unique ID of the run

    try:
        # [EXPERIMENTAL] GetRunHistory: Get the history for a single job run
        api_response = await api_instance.get_run_history(run_id)
        print("The response of JobsApi->get_run_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_run_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The unique ID of the run | 

### Return type

[**JobRunResult**](JobRunResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedules_for_a_job**
> ResourceListOfScheduleDefinition get_schedules_for_a_job(scope, code)

[EXPERIMENTAL] GetSchedulesForAJob: Get all the schedules for a single job

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_scheduler
from finbourne_scheduler.rest import ApiException
from finbourne_scheduler.models.resource_list_of_schedule_definition import ResourceListOfScheduleDefinition
from pprint import pprint

from finbourne_scheduler import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the finbourne_scheduler ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-ci.lusid.com/scheduler2"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_scheduler.JobsApi)
    scope = 'scope_example' # str | The scope of the job
    code = 'code_example' # str | The code of the job

    try:
        # [EXPERIMENTAL] GetSchedulesForAJob: Get all the schedules for a single job
        api_response = await api_instance.get_schedules_for_a_job(scope, code)
        print("The response of JobsApi->get_schedules_for_a_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_schedules_for_a_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the job | 
 **code** | **str**| The code of the job | 

### Return type

[**ResourceListOfScheduleDefinition**](ResourceListOfScheduleDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jobs**
> ResourceListOfJobDefinition list_jobs(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

[EXPERIMENTAL] ListJobs: List the available jobs

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_scheduler
from finbourne_scheduler.rest import ApiException
from finbourne_scheduler.models.resource_list_of_job_definition import ResourceListOfJobDefinition
from pprint import pprint

from finbourne_scheduler import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the finbourne_scheduler ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-ci.lusid.com/scheduler2"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_scheduler.JobsApi)
    page = 'page_example' # str | The pagination token to use to continue listing instruments from a previous call to list instruments.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
    sort_by = ['sort_by_example'] # List[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
    start = 56 # int | When paginating, skip this number of results. (optional)
    limit = 2000 # int | When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified. Maximum is 5000. (optional) (default to 2000)
    filter = 'filter_example' # str | Expression to filter the result set. (optional)

    try:
        # [EXPERIMENTAL] ListJobs: List the available jobs
        api_response = await api_instance.list_jobs(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
        print("The response of JobsApi->list_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->list_jobs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| The pagination token to use to continue listing instruments from a previous call to list instruments.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **sort_by** | [**List[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified. Maximum is 5000. | [optional] [default to 2000]
 **filter** | **str**| Expression to filter the result set. | [optional] 

### Return type

[**ResourceListOfJobDefinition**](ResourceListOfJobDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_job**
> StartJobResponse run_job(scope, code, start_job_request)

[EXPERIMENTAL] RunJob: Run a job immediately

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_scheduler
from finbourne_scheduler.rest import ApiException
from finbourne_scheduler.models.start_job_request import StartJobRequest
from finbourne_scheduler.models.start_job_response import StartJobResponse
from pprint import pprint

from finbourne_scheduler import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the finbourne_scheduler ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-ci.lusid.com/scheduler2"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_scheduler.JobsApi)
    scope = 'scope_example' # str | The scope of the job
    code = 'code_example' # str | The code of the job
    start_job_request = {"arguments":{"ExchangeCode":"XLON"},"notifications":[{"fireOn":"Completed","transport":"Email","destination":["Team A"]}],"useAsAuth":"job auth userId"} # StartJobRequest | The request for starting job

    try:
        # [EXPERIMENTAL] RunJob: Run a job immediately
        api_response = await api_instance.run_job(scope, code, start_job_request)
        print("The response of JobsApi->run_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->run_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the job | 
 **code** | **str**| The code of the job | 
 **start_job_request** | [**StartJobRequest**](StartJobRequest.md)| The request for starting job | 

### Return type

[**StartJobResponse**](StartJobResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job**
> JobDefinition update_job(scope, code, update_job_request)

[EXPERIMENTAL] UpdateJob: Update a JobDefinition

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_scheduler
from finbourne_scheduler.rest import ApiException
from finbourne_scheduler.models.job_definition import JobDefinition
from finbourne_scheduler.models.update_job_request import UpdateJobRequest
from pprint import pprint

from finbourne_scheduler import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the finbourne_scheduler ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-ci.lusid.com/scheduler2"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_scheduler.JobsApi)
    scope = 'scope_example' # str | 
    code = 'code_example' # str | 
    update_job_request = {"name":"Updated job name","author":"Job author","description":"Updated job description","imageName":"Updated image name","imageTag":"Updated image tag","ttl":250,"minCpu":"2","maxCpu":"4","minMemory":"0.5Mi","maxMemory":"500Mi","argumentDefinitions":{"UpdatedSecret":{"dataType":"SecureString","required":true,"description":"Database credentials","order":1,"constraints":"None","passedAs":"EnvironmentVariable"},"UpdatedArgument":{"dataType":"String","required":true,"description":"Command line argument","order":2,"constraints":"None","passedAs":"CommandLine","defaultValue":"Update default value"}},"commandLineArgumentSeparator":" ","requiredResources":{"lusidApis":["Shrine, IBOR"],"lusidFileSystem":[],"externalCalls":["AWS"]}} # UpdateJobRequest | 

    try:
        # [EXPERIMENTAL] UpdateJob: Update a JobDefinition
        api_response = await api_instance.update_job(scope, code, update_job_request)
        print("The response of JobsApi->update_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->update_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | 
 **code** | **str**|  | 
 **update_job_request** | [**UpdateJobRequest**](UpdateJobRequest.md)|  | 

### Return type

[**JobDefinition**](JobDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

