# lusid_scheduler.SchedulesApi

All URIs are relative to *https://fbn-prd.lusid.com/scheduler2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_schedule**](SchedulesApi.md#create_schedule) | **POST** /api/schedules | CreateSchedule: Create a Schedule for a job
[**delete_schedule**](SchedulesApi.md#delete_schedule) | **DELETE** /api/schedules/{scope}/{code} | DeleteSchedule: Delete a schedule
[**enabled_schedule**](SchedulesApi.md#enabled_schedule) | **PUT** /api/schedules/{scope}/{code}/enabled | EnabledSchedule: Enable/disable a schedule
[**get_schedule**](SchedulesApi.md#get_schedule) | **GET** /api/schedules/{scope}/{code} | GetSchedule: Get a single Schedule
[**list_schedules**](SchedulesApi.md#list_schedules) | **GET** /api/schedules | ListSchedules: List the available Schedules
[**run_schedule**](SchedulesApi.md#run_schedule) | **POST** /api/schedules/{scope}/{code}/$run | RunSchedule: Run a schedule immediately
[**update_schedule**](SchedulesApi.md#update_schedule) | **PUT** /api/schedules/{scope}/{code} | UpdateSchedule: Update a schedule.


# **create_schedule**
> ScheduleDefinition create_schedule(create_schedule_request)

CreateSchedule: Create a Schedule for a job

### Example

```python
from lusid_scheduler.exceptions import ApiException
from lusid_scheduler.extensions.configuration_options import ConfigurationOptions
from lusid_scheduler.models import *
from pprint import pprint
from lusid_scheduler import (
    SyncApiClientFactory,
    SchedulesApi
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
    api_instance = api_client_factory.build(SchedulesApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_schedule_request = CreateScheduleRequest.from_json("")
    # create_schedule_request = CreateScheduleRequest.from_dict({})
    create_schedule_request = CreateScheduleRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_schedule(create_schedule_request, opts=opts)

        # CreateSchedule: Create a Schedule for a job
        api_response = api_instance.create_schedule(create_schedule_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SchedulesApi->create_schedule: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_schedule_request** | [**CreateScheduleRequest**](CreateScheduleRequest.md)|  | 

### Return type

[**ScheduleDefinition**](ScheduleDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created schedule |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_schedule**
> delete_schedule(scope, code)

DeleteSchedule: Delete a schedule

### Example

```python
from lusid_scheduler.exceptions import ApiException
from lusid_scheduler.extensions.configuration_options import ConfigurationOptions
from lusid_scheduler.models import *
from pprint import pprint
from lusid_scheduler import (
    SyncApiClientFactory,
    SchedulesApi
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
    api_instance = api_client_factory.build(SchedulesApi)
    scope = 'scope_example' # str | Scope of the schedule to be deleted
    code = 'code_example' # str | Code of the schedule to be deleted

    try:
        # uncomment the below to set overrides at the request level
        #  api_instance.delete_schedule(scope, code, opts=opts)

        # DeleteSchedule: Delete a schedule
        api_instance.delete_schedule(scope, code)
    except ApiException as e:
        print("Exception when calling SchedulesApi->delete_schedule: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the schedule to be deleted | 
 **code** | **str**| Code of the schedule to be deleted | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **enabled_schedule**
> ScheduleDefinition enabled_schedule(scope, code, enable)

EnabledSchedule: Enable/disable a schedule

### Example

```python
from lusid_scheduler.exceptions import ApiException
from lusid_scheduler.extensions.configuration_options import ConfigurationOptions
from lusid_scheduler.models import *
from pprint import pprint
from lusid_scheduler import (
    SyncApiClientFactory,
    SchedulesApi
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
    api_instance = api_client_factory.build(SchedulesApi)
    scope = 'scope_example' # str | Scope of the schedule to be enabled/disabled
    code = 'code_example' # str | Code of the schedule to be enabled/disabled
    enable = True # bool | Specify whether to enable or disable the schedule

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.enabled_schedule(scope, code, enable, opts=opts)

        # EnabledSchedule: Enable/disable a schedule
        api_response = api_instance.enabled_schedule(scope, code, enable)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SchedulesApi->enabled_schedule: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the schedule to be enabled/disabled | 
 **code** | **str**| Code of the schedule to be enabled/disabled | 
 **enable** | **bool**| Specify whether to enable or disable the schedule | 

### Return type

[**ScheduleDefinition**](ScheduleDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_schedule**
> ScheduleDefinition get_schedule(scope, code)

GetSchedule: Get a single Schedule

### Example

```python
from lusid_scheduler.exceptions import ApiException
from lusid_scheduler.extensions.configuration_options import ConfigurationOptions
from lusid_scheduler.models import *
from pprint import pprint
from lusid_scheduler import (
    SyncApiClientFactory,
    SchedulesApi
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
    api_instance = api_client_factory.build(SchedulesApi)
    scope = 'scope_example' # str | The scope of Schedule
    code = 'code_example' # str | The code of the Schedule

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_schedule(scope, code, opts=opts)

        # GetSchedule: Get a single Schedule
        api_response = api_instance.get_schedule(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SchedulesApi->get_schedule: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of Schedule | 
 **code** | **str**| The code of the Schedule | 

### Return type

[**ScheduleDefinition**](ScheduleDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_schedules**
> ResourceListOfScheduleDefinition list_schedules(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

ListSchedules: List the available Schedules

### Example

```python
from lusid_scheduler.exceptions import ApiException
from lusid_scheduler.extensions.configuration_options import ConfigurationOptions
from lusid_scheduler.models import *
from pprint import pprint
from lusid_scheduler import (
    SyncApiClientFactory,
    SchedulesApi
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
    api_instance = api_client_factory.build(SchedulesApi)
    page = 'page_example' # str | The pagination token to use to continue listing instruments from a previous call to list instruments.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
    sort_by = ['sort_by_example'] # List[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
    start = 56 # int | When paginating, skip this number of results. (optional)
    limit = 2000 # int | When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified. Maximum is 5000. (optional) (default to 2000)
    filter = 'filter_example' # str | Expression to filter the result set. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_schedules(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter, opts=opts)

        # ListSchedules: List the available Schedules
        api_response = api_instance.list_schedules(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SchedulesApi->list_schedules: %s\n" % e)

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

[**ResourceListOfScheduleDefinition**](ResourceListOfScheduleDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **run_schedule**
> StartScheduleResponse run_schedule(scope, code)

RunSchedule: Run a schedule immediately

### Example

```python
from lusid_scheduler.exceptions import ApiException
from lusid_scheduler.extensions.configuration_options import ConfigurationOptions
from lusid_scheduler.models import *
from pprint import pprint
from lusid_scheduler import (
    SyncApiClientFactory,
    SchedulesApi
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
    api_instance = api_client_factory.build(SchedulesApi)
    scope = 'scope_example' # str | The schedule scope
    code = 'code_example' # str | The schedule cde

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.run_schedule(scope, code, opts=opts)

        # RunSchedule: Run a schedule immediately
        api_response = api_instance.run_schedule(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SchedulesApi->run_schedule: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The schedule scope | 
 **code** | **str**| The schedule cde | 

### Return type

[**StartScheduleResponse**](StartScheduleResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_schedule**
> ScheduleDefinition update_schedule(scope, code, update_schedule_request)

UpdateSchedule: Update a schedule.

### Example

```python
from lusid_scheduler.exceptions import ApiException
from lusid_scheduler.extensions.configuration_options import ConfigurationOptions
from lusid_scheduler.models import *
from pprint import pprint
from lusid_scheduler import (
    SyncApiClientFactory,
    SchedulesApi
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
    api_instance = api_client_factory.build(SchedulesApi)
    scope = 'scope_example' # str | Scope of the schedule to be updated
    code = 'code_example' # str | Code of the schedule to be updated

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_schedule_request = UpdateScheduleRequest.from_json("")
    # update_schedule_request = UpdateScheduleRequest.from_dict({})
    update_schedule_request = UpdateScheduleRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_schedule(scope, code, update_schedule_request, opts=opts)

        # UpdateSchedule: Update a schedule.
        api_response = api_instance.update_schedule(scope, code, update_schedule_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SchedulesApi->update_schedule: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the schedule to be updated | 
 **code** | **str**| Code of the schedule to be updated | 
 **update_schedule_request** | [**UpdateScheduleRequest**](UpdateScheduleRequest.md)| The updated schedule | 

### Return type

[**ScheduleDefinition**](ScheduleDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

