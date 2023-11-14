# lusid_scheduler.SchedulesApi

All URIs are relative to *https://fbn-prd.lusid.com/scheduler2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_schedule**](SchedulesApi.md#create_schedule) | **POST** /api/schedules | [EXPERIMENTAL] CreateSchedule: Create a Schedule for a job
[**delete_schedule**](SchedulesApi.md#delete_schedule) | **DELETE** /api/schedules/{scope}/{code} | [EXPERIMENTAL] DeleteSchedule: Delete a schedule
[**enabled_schedule**](SchedulesApi.md#enabled_schedule) | **PUT** /api/schedules/{scope}/{code}/enabled | [EXPERIMENTAL] EnabledSchedule: Enable/disable a schedule
[**get_schedule**](SchedulesApi.md#get_schedule) | **GET** /api/schedules/{scope}/{code} | [EXPERIMENTAL] GetSchedule: Get a single Schedule
[**list_schedules**](SchedulesApi.md#list_schedules) | **GET** /api/schedules | [EXPERIMENTAL] ListSchedules: List the available Schedules
[**run_schedule**](SchedulesApi.md#run_schedule) | **POST** /api/schedules/{scope}/{code}/$run | [EXPERIMENTAL] RunSchedule: Run a schedule immediately
[**update_schedule**](SchedulesApi.md#update_schedule) | **PUT** /api/schedules/{scope}/{code} | [EXPERIMENTAL] UpdateSchedule: Update a schedule.


# **create_schedule**
> ScheduleDefinition create_schedule(create_schedule_request)

[EXPERIMENTAL] CreateSchedule: Create a Schedule for a job

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid_scheduler
from lusid_scheduler.rest import ApiException
from lusid_scheduler.models.create_schedule_request import CreateScheduleRequest
from lusid_scheduler.models.schedule_definition import ScheduleDefinition
from pprint import pprint

from lusid_scheduler import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid_scheduler ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/scheduler2"
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
    api_instance = api_client_factory.build(lusid_scheduler.SchedulesApi)
    create_schedule_request = {"scheduleId":{"scope":"ScheduleScope","code":"ScheduleCode"},"jobId":{"scope":"JobScope","code":"JobCode"},"name":"Schedule name","description":"Schedule description","author":"Schedule author","owner":"Schedule owner","arguments":{"Argument":"Argument value"},"trigger":{"timeTrigger":{"expression":"0 0 5 ? * 3","timeZone":"UTC"}},"notifications":[{"fireOn":"Completed","transport":"Email","destination":["destination"]},{"fireOn":"Failed","transport":"SMS","destination":["destination1","destination2"]}],"enabled":true,"useAsAuth":"Schedule auth userId"} # CreateScheduleRequest | 

    try:
        # [EXPERIMENTAL] CreateSchedule: Create a Schedule for a job
        api_response = await api_instance.create_schedule(create_schedule_request)
        print("The response of SchedulesApi->create_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->create_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_schedule_request** | [**CreateScheduleRequest**](CreateScheduleRequest.md)|  | 

### Return type

[**ScheduleDefinition**](ScheduleDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created schedule |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_schedule**
> delete_schedule(scope, code)

[EXPERIMENTAL] DeleteSchedule: Delete a schedule

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid_scheduler
from lusid_scheduler.rest import ApiException
from pprint import pprint

from lusid_scheduler import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid_scheduler ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/scheduler2"
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
    api_instance = api_client_factory.build(lusid_scheduler.SchedulesApi)
    scope = 'scope_example' # str | Scope of the schedule to be deleted
    code = 'code_example' # str | Code of the schedule to be deleted

    try:
        # [EXPERIMENTAL] DeleteSchedule: Delete a schedule
        await api_instance.delete_schedule(scope, code)
    except Exception as e:
        print("Exception when calling SchedulesApi->delete_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the schedule to be deleted | 
 **code** | **str**| Code of the schedule to be deleted | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enabled_schedule**
> ScheduleDefinition enabled_schedule(scope, code, enable)

[EXPERIMENTAL] EnabledSchedule: Enable/disable a schedule

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid_scheduler
from lusid_scheduler.rest import ApiException
from lusid_scheduler.models.schedule_definition import ScheduleDefinition
from pprint import pprint

from lusid_scheduler import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid_scheduler ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/scheduler2"
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
    api_instance = api_client_factory.build(lusid_scheduler.SchedulesApi)
    scope = 'scope_example' # str | Scope of the schedule to be enabled/disabled
    code = 'code_example' # str | Code of the schedule to be enabled/disabled
    enable = True # bool | Specify whether to enable or disable the schedule

    try:
        # [EXPERIMENTAL] EnabledSchedule: Enable/disable a schedule
        api_response = await api_instance.enabled_schedule(scope, code, enable)
        print("The response of SchedulesApi->enabled_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->enabled_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the schedule to be enabled/disabled | 
 **code** | **str**| Code of the schedule to be enabled/disabled | 
 **enable** | **bool**| Specify whether to enable or disable the schedule | 

### Return type

[**ScheduleDefinition**](ScheduleDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedule**
> ScheduleDefinition get_schedule(scope, code)

[EXPERIMENTAL] GetSchedule: Get a single Schedule

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid_scheduler
from lusid_scheduler.rest import ApiException
from lusid_scheduler.models.schedule_definition import ScheduleDefinition
from pprint import pprint

from lusid_scheduler import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid_scheduler ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/scheduler2"
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
    api_instance = api_client_factory.build(lusid_scheduler.SchedulesApi)
    scope = 'scope_example' # str | The scope of Schedule
    code = 'code_example' # str | The code of the Schedule

    try:
        # [EXPERIMENTAL] GetSchedule: Get a single Schedule
        api_response = await api_instance.get_schedule(scope, code)
        print("The response of SchedulesApi->get_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->get_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of Schedule | 
 **code** | **str**| The code of the Schedule | 

### Return type

[**ScheduleDefinition**](ScheduleDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_schedules**
> ResourceListOfScheduleDefinition list_schedules(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

[EXPERIMENTAL] ListSchedules: List the available Schedules

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid_scheduler
from lusid_scheduler.rest import ApiException
from lusid_scheduler.models.resource_list_of_schedule_definition import ResourceListOfScheduleDefinition
from pprint import pprint

from lusid_scheduler import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid_scheduler ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/scheduler2"
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
    api_instance = api_client_factory.build(lusid_scheduler.SchedulesApi)
    page = 'page_example' # str | The pagination token to use to continue listing instruments from a previous call to list instruments.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
    sort_by = ['sort_by_example'] # List[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
    start = 56 # int | When paginating, skip this number of results. (optional)
    limit = 2000 # int | When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified. Maximum is 5000. (optional) (default to 2000)
    filter = 'filter_example' # str | Expression to filter the result set. (optional)

    try:
        # [EXPERIMENTAL] ListSchedules: List the available Schedules
        api_response = await api_instance.list_schedules(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
        print("The response of SchedulesApi->list_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->list_schedules: %s\n" % e)
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

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_schedule**
> StartScheduleResponse run_schedule(scope, code)

[EXPERIMENTAL] RunSchedule: Run a schedule immediately

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid_scheduler
from lusid_scheduler.rest import ApiException
from lusid_scheduler.models.start_schedule_response import StartScheduleResponse
from pprint import pprint

from lusid_scheduler import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid_scheduler ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/scheduler2"
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
    api_instance = api_client_factory.build(lusid_scheduler.SchedulesApi)
    scope = 'scope_example' # str | The schedule scope
    code = 'code_example' # str | The schedule cde

    try:
        # [EXPERIMENTAL] RunSchedule: Run a schedule immediately
        api_response = await api_instance.run_schedule(scope, code)
        print("The response of SchedulesApi->run_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->run_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The schedule scope | 
 **code** | **str**| The schedule cde | 

### Return type

[**StartScheduleResponse**](StartScheduleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_schedule**
> ScheduleDefinition update_schedule(scope, code, update_schedule_request)

[EXPERIMENTAL] UpdateSchedule: Update a schedule.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid_scheduler
from lusid_scheduler.rest import ApiException
from lusid_scheduler.models.schedule_definition import ScheduleDefinition
from lusid_scheduler.models.update_schedule_request import UpdateScheduleRequest
from pprint import pprint

from lusid_scheduler import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid_scheduler ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/scheduler2"
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
    api_instance = api_client_factory.build(lusid_scheduler.SchedulesApi)
    scope = 'scope_example' # str | Scope of the schedule to be updated
    code = 'code_example' # str | Code of the schedule to be updated
    update_schedule_request = {"jobId":{"scope":"JobScope","code":"JobCode"},"name":"UpdatedSchedule","description":"Updated description","author":"Updated author","owner":"Updated owner","arguments":{"UpdatedArgument":"Updated value"},"trigger":{"timeTrigger":{"expression":"0 0 5 ? * 3","timeZone":"UTC"}},"notifications":[{"fireOn":"Completed","transport":"Email","destination":["destination"]},{"fireOn":"Failed","transport":"SMS","destination":["destination1","destination2"]}],"enabled":true,"useAsAuth":"Schedule auth userId"} # UpdateScheduleRequest | The updated schedule

    try:
        # [EXPERIMENTAL] UpdateSchedule: Update a schedule.
        api_response = await api_instance.update_schedule(scope, code, update_schedule_request)
        print("The response of SchedulesApi->update_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->update_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the schedule to be updated | 
 **code** | **str**| Code of the schedule to be updated | 
 **update_schedule_request** | [**UpdateScheduleRequest**](UpdateScheduleRequest.md)| The updated schedule | 

### Return type

[**ScheduleDefinition**](ScheduleDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

