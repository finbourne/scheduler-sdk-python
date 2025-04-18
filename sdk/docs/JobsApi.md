# lusid_scheduler.JobsApi

All URIs are relative to *https://fbn-prd.lusid.com/scheduler2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_job**](JobsApi.md#create_job) | **POST** /api/jobs | CreateJob: Create a new job
[**delete_job**](JobsApi.md#delete_job) | **DELETE** /api/jobs/{scope}/{code} | DeleteJob: Delete a job
[**get_history**](JobsApi.md#get_history) | **GET** /api/jobs/history | GetHistory: Get the history of job runs
[**get_job_console_output**](JobsApi.md#get_job_console_output) | **GET** /api/jobs/history/{runId}/console | GetJobConsoleOutput: Gets the console output of a specific job run
[**get_run_history**](JobsApi.md#get_run_history) | **GET** /api/jobs/history/{runId} | GetRunHistory: Get the history for a single job run
[**get_schedules_for_a_job**](JobsApi.md#get_schedules_for_a_job) | **GET** /api/jobs/{scope}/{code}/schedules | GetSchedulesForAJob: Get all the schedules for a single job
[**list_jobs**](JobsApi.md#list_jobs) | **GET** /api/jobs | ListJobs: List the available jobs
[**run_job**](JobsApi.md#run_job) | **POST** /api/jobs/{scope}/{code}/$run | RunJob: Run a job immediately
[**update_job**](JobsApi.md#update_job) | **PUT** /api/jobs/{scope}/{code} | UpdateJob: Update a JobDefinition


# **create_job**
> JobDefinition create_job(create_job_request)

CreateJob: Create a new job

### Example

```python
from lusid_scheduler.exceptions import ApiException
from lusid_scheduler.extensions.configuration_options import ConfigurationOptions
from lusid_scheduler.models import *
from pprint import pprint
from lusid_scheduler import (
    SyncApiClientFactory,
    JobsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "schedulerUrl":"https://<your-domain>.lusid.com/scheduler2",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid_scheduler SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(JobsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_job_request = CreateJobRequest.from_json("")
    # create_job_request = CreateJobRequest.from_dict({})
    create_job_request = CreateJobRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_job(create_job_request, opts=opts)

        # CreateJob: Create a new job
        api_response = api_instance.create_job(create_job_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling JobsApi->create_job: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_job_request** | [**CreateJobRequest**](CreateJobRequest.md)| The request to create a new job | 

### Return type

[**JobDefinition**](JobDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_job**
> ResourceListOfScheduleDefinition delete_job(scope, code)

DeleteJob: Delete a job

### Example

```python
from lusid_scheduler.exceptions import ApiException
from lusid_scheduler.extensions.configuration_options import ConfigurationOptions
from lusid_scheduler.models import *
from pprint import pprint
from lusid_scheduler import (
    SyncApiClientFactory,
    JobsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "schedulerUrl":"https://<your-domain>.lusid.com/scheduler2",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid_scheduler SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(JobsApi)
    scope = 'scope_example' # str | The scope of the job
    code = 'code_example' # str | The code of the job

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_job(scope, code, opts=opts)

        # DeleteJob: Delete a job
        api_response = api_instance.delete_job(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling JobsApi->delete_job: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the job | 
 **code** | **str**| The code of the job | 

### Return type

[**ResourceListOfScheduleDefinition**](ResourceListOfScheduleDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_history**
> ResourceListOfJobHistory get_history(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

GetHistory: Get the history of job runs

### Example

```python
from lusid_scheduler.exceptions import ApiException
from lusid_scheduler.extensions.configuration_options import ConfigurationOptions
from lusid_scheduler.models import *
from pprint import pprint
from lusid_scheduler import (
    SyncApiClientFactory,
    JobsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "schedulerUrl":"https://<your-domain>.lusid.com/scheduler2",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid_scheduler SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(JobsApi)
    page = 'page_example' # str | The pagination token to use to continue listing instruments from a previous call to list instruments.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
    sort_by = ['sort_by_example'] # List[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
    start = 56 # int | This field is obsolete, the value of this field would not be considered. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified. Maximum is 5000. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_history(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter, opts=opts)

        # GetHistory: Get the history of job runs
        api_response = api_instance.get_history(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling JobsApi->get_history: %s\n" % e)

main()
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

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_job_console_output**
> str get_job_console_output(run_id)

GetJobConsoleOutput: Gets the console output of a specific job run

### Example

```python
from lusid_scheduler.exceptions import ApiException
from lusid_scheduler.extensions.configuration_options import ConfigurationOptions
from lusid_scheduler.models import *
from pprint import pprint
from lusid_scheduler import (
    SyncApiClientFactory,
    JobsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "schedulerUrl":"https://<your-domain>.lusid.com/scheduler2",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid_scheduler SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(JobsApi)
    run_id = 'run_id_example' # str | The RunId of the job run

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_job_console_output(run_id, opts=opts)

        # GetJobConsoleOutput: Gets the console output of a specific job run
        api_response = api_instance.get_job_console_output(run_id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling JobsApi->get_job_console_output: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The RunId of the job run | 

### Return type

**str**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_run_history**
> JobRunResult get_run_history(run_id)

GetRunHistory: Get the history for a single job run

### Example

```python
from lusid_scheduler.exceptions import ApiException
from lusid_scheduler.extensions.configuration_options import ConfigurationOptions
from lusid_scheduler.models import *
from pprint import pprint
from lusid_scheduler import (
    SyncApiClientFactory,
    JobsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "schedulerUrl":"https://<your-domain>.lusid.com/scheduler2",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid_scheduler SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(JobsApi)
    run_id = 'run_id_example' # str | The unique ID of the run

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_run_history(run_id, opts=opts)

        # GetRunHistory: Get the history for a single job run
        api_response = api_instance.get_run_history(run_id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling JobsApi->get_run_history: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The unique ID of the run | 

### Return type

[**JobRunResult**](JobRunResult.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_schedules_for_a_job**
> ResourceListOfScheduleDefinition get_schedules_for_a_job(scope, code)

GetSchedulesForAJob: Get all the schedules for a single job

### Example

```python
from lusid_scheduler.exceptions import ApiException
from lusid_scheduler.extensions.configuration_options import ConfigurationOptions
from lusid_scheduler.models import *
from pprint import pprint
from lusid_scheduler import (
    SyncApiClientFactory,
    JobsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "schedulerUrl":"https://<your-domain>.lusid.com/scheduler2",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid_scheduler SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(JobsApi)
    scope = 'scope_example' # str | The scope of the job
    code = 'code_example' # str | The code of the job

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_schedules_for_a_job(scope, code, opts=opts)

        # GetSchedulesForAJob: Get all the schedules for a single job
        api_response = api_instance.get_schedules_for_a_job(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling JobsApi->get_schedules_for_a_job: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the job | 
 **code** | **str**| The code of the job | 

### Return type

[**ResourceListOfScheduleDefinition**](ResourceListOfScheduleDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_jobs**
> ResourceListOfJobDefinition list_jobs(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

ListJobs: List the available jobs

### Example

```python
from lusid_scheduler.exceptions import ApiException
from lusid_scheduler.extensions.configuration_options import ConfigurationOptions
from lusid_scheduler.models import *
from pprint import pprint
from lusid_scheduler import (
    SyncApiClientFactory,
    JobsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "schedulerUrl":"https://<your-domain>.lusid.com/scheduler2",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid_scheduler SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(JobsApi)
    page = 'page_example' # str | The pagination token to use to continue listing instruments from a previous call to list instruments.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
    sort_by = ['sort_by_example'] # List[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
    start = 56 # int | When paginating, skip this number of results. (optional)
    limit = 2000 # int | When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified. Maximum is 5000. (optional) (default to 2000)
    filter = 'filter_example' # str | Expression to filter the result set. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_jobs(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter, opts=opts)

        # ListJobs: List the available jobs
        api_response = api_instance.list_jobs(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling JobsApi->list_jobs: %s\n" % e)

main()
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

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **run_job**
> StartJobResponse run_job(scope, code, start_job_request)

RunJob: Run a job immediately

### Example

```python
from lusid_scheduler.exceptions import ApiException
from lusid_scheduler.extensions.configuration_options import ConfigurationOptions
from lusid_scheduler.models import *
from pprint import pprint
from lusid_scheduler import (
    SyncApiClientFactory,
    JobsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "schedulerUrl":"https://<your-domain>.lusid.com/scheduler2",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid_scheduler SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(JobsApi)
    scope = 'scope_example' # str | The scope of the job
    code = 'code_example' # str | The code of the job

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # start_job_request = StartJobRequest.from_json("")
    # start_job_request = StartJobRequest.from_dict({})
    start_job_request = StartJobRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.run_job(scope, code, start_job_request, opts=opts)

        # RunJob: Run a job immediately
        api_response = api_instance.run_job(scope, code, start_job_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling JobsApi->run_job: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the job | 
 **code** | **str**| The code of the job | 
 **start_job_request** | [**StartJobRequest**](StartJobRequest.md)| The request for starting job | 

### Return type

[**StartJobResponse**](StartJobResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_job**
> JobDefinition update_job(scope, code, update_job_request)

UpdateJob: Update a JobDefinition

### Example

```python
from lusid_scheduler.exceptions import ApiException
from lusid_scheduler.extensions.configuration_options import ConfigurationOptions
from lusid_scheduler.models import *
from pprint import pprint
from lusid_scheduler import (
    SyncApiClientFactory,
    JobsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "schedulerUrl":"https://<your-domain>.lusid.com/scheduler2",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid_scheduler SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(JobsApi)
    scope = 'scope_example' # str | 
    code = 'code_example' # str | 

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_job_request = UpdateJobRequest.from_json("")
    # update_job_request = UpdateJobRequest.from_dict({})
    update_job_request = UpdateJobRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_job(scope, code, update_job_request, opts=opts)

        # UpdateJob: Update a JobDefinition
        api_response = api_instance.update_job(scope, code, update_job_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling JobsApi->update_job: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | 
 **code** | **str**|  | 
 **update_job_request** | [**UpdateJobRequest**](UpdateJobRequest.md)|  | 

### Return type

[**JobDefinition**](JobDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

