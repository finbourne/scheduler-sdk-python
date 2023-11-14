# lusid_scheduler.ImagesApi

All URIs are relative to *https://fbn-prd.lusid.com/scheduler2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_image**](ImagesApi.md#delete_image) | **DELETE** /api/images/{name} | [EXPERIMENTAL] DeleteImage: Delete a Docker Image
[**download_image**](ImagesApi.md#download_image) | **GET** /api/images/{name}/contents | [EXPERIMENTAL] DownloadImage: Download Docker Image
[**get_image**](ImagesApi.md#get_image) | **GET** /api/images/{name} | [EXPERIMENTAL] GetImage: Get metadata of a Docker Image
[**list_images**](ImagesApi.md#list_images) | **GET** /api/images/repository/{name} | [EXPERIMENTAL] ListImages: List all images under same image repository
[**list_repositories**](ImagesApi.md#list_repositories) | **GET** /api/images/repository | [EXPERIMENTAL] ListRepositories: List all Docker image repositories
[**upload_image**](ImagesApi.md#upload_image) | **POST** /api/images | [EXPERIMENTAL] UploadImage: Upload a Docker Image used for Scheduler jobs


# **delete_image**
> str delete_image(name)

[EXPERIMENTAL] DeleteImage: Delete a Docker Image

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
    api_instance = api_client_factory.build(lusid_scheduler.ImagesApi)
    name = 'name_example' # str | The name and tag of the image. Format \"ExampleImageName:0.1\"

    try:
        # [EXPERIMENTAL] DeleteImage: Delete a Docker Image
        api_response = await api_instance.delete_image(name)
        print("The response of ImagesApi->delete_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->delete_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name and tag of the image. Format \&quot;ExampleImageName:0.1\&quot; | 

### Return type

**str**

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
**404** | No image with this name and tag exists |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_image**
> bytearray download_image(name)

[EXPERIMENTAL] DownloadImage: Download Docker Image

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
    api_instance = api_client_factory.build(lusid_scheduler.ImagesApi)
    name = 'name_example' # str | The name and tag of the image of the image. Format \"ExampleImageName:latest\"

    try:
        # [EXPERIMENTAL] DownloadImage: Download Docker Image
        api_response = await api_instance.download_image(name)
        print("The response of ImagesApi->download_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->download_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name and tag of the image of the image. Format \&quot;ExampleImageName:latest\&quot; | 

### Return type

**bytearray**

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

# **get_image**
> Image get_image(name)

[EXPERIMENTAL] GetImage: Get metadata of a Docker Image

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid_scheduler
from lusid_scheduler.rest import ApiException
from lusid_scheduler.models.image import Image
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
    api_instance = api_client_factory.build(lusid_scheduler.ImagesApi)
    name = 'name_example' # str | The name and tag of a Docker image. Format \"ExampleImageName:latest\"

    try:
        # [EXPERIMENTAL] GetImage: Get metadata of a Docker Image
        api_response = await api_instance.get_image(name)
        print("The response of ImagesApi->get_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->get_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name and tag of a Docker image. Format \&quot;ExampleImageName:latest\&quot; | 

### Return type

[**Image**](Image.md)

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

# **list_images**
> ResourceListOfImageSummary list_images(name, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

[EXPERIMENTAL] ListImages: List all images under same image repository

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid_scheduler
from lusid_scheduler.rest import ApiException
from lusid_scheduler.models.resource_list_of_image_summary import ResourceListOfImageSummary
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
    api_instance = api_client_factory.build(lusid_scheduler.ImagesApi)
    name = 'name_example' # str | The name of the Repository
    page = 'page_example' # str | The pagination token to use to continue listing images from a previous call to list images.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
    sort_by = ['sort_by_example'] # List[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
    start = 56 # int | When paginating, skip this number of results. (optional)
    limit = 2000 # int | When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified. Maximum is 5000. (optional) (default to 2000)
    filter = 'filter_example' # str | Expression to filter the result set. (optional)

    try:
        # [EXPERIMENTAL] ListImages: List all images under same image repository
        api_response = await api_instance.list_images(name, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
        print("The response of ImagesApi->list_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->list_images: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Repository | 
 **page** | **str**| The pagination token to use to continue listing images from a previous call to list images.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **sort_by** | [**List[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified. Maximum is 5000. | [optional] [default to 2000]
 **filter** | **str**| Expression to filter the result set. | [optional] 

### Return type

[**ResourceListOfImageSummary**](ResourceListOfImageSummary.md)

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

# **list_repositories**
> ResourceListOfRepository list_repositories(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

[EXPERIMENTAL] ListRepositories: List all Docker image repositories

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid_scheduler
from lusid_scheduler.rest import ApiException
from lusid_scheduler.models.resource_list_of_repository import ResourceListOfRepository
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
    api_instance = api_client_factory.build(lusid_scheduler.ImagesApi)
    page = 'page_example' # str | The pagination token to use to continue listing images from a previous call to list images.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
    sort_by = ['sort_by_example'] # List[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
    start = 56 # int | When paginating, skip this number of results. (optional)
    limit = 2000 # int | When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified. Maximum is 5000. (optional) (default to 2000)
    filter = 'filter_example' # str | Expression to filter the result set. (optional)

    try:
        # [EXPERIMENTAL] ListRepositories: List all Docker image repositories
        api_response = await api_instance.list_repositories(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
        print("The response of ImagesApi->list_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->list_repositories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| The pagination token to use to continue listing images from a previous call to list images.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **sort_by** | [**List[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified. Maximum is 5000. | [optional] [default to 2000]
 **filter** | **str**| Expression to filter the result set. | [optional] 

### Return type

[**ResourceListOfRepository**](ResourceListOfRepository.md)

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

# **upload_image**
> UploadImageInstructions upload_image(upload_image_request)

[EXPERIMENTAL] UploadImage: Upload a Docker Image used for Scheduler jobs

Every image must have at least one tag. Note: your image will not be available until the returned Docker commands are executed.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid_scheduler
from lusid_scheduler.rest import ApiException
from lusid_scheduler.models.upload_image_instructions import UploadImageInstructions
from lusid_scheduler.models.upload_image_request import UploadImageRequest
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
    api_instance = api_client_factory.build(lusid_scheduler.ImagesApi)
    upload_image_request = {"imageName":"example-image-name:0.0.1"} # UploadImageRequest | Request to upload image

    try:
        # [EXPERIMENTAL] UploadImage: Upload a Docker Image used for Scheduler jobs
        api_response = await api_instance.upload_image(upload_image_request)
        print("The response of ImagesApi->upload_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->upload_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_image_request** | [**UploadImageRequest**](UploadImageRequest.md)| Request to upload image | 

### Return type

[**UploadImageInstructions**](UploadImageInstructions.md)

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

