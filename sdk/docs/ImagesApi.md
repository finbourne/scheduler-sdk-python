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

```python
import asyncio
from lusid_scheduler.exceptions import ApiException
from lusid_scheduler.extensions.configuration_options import ConfigurationOptions
from lusid_scheduler.models import *
from pprint import pprint
from lusid_scheduler import (
    ApiClientFactory,
    ImagesApi
)

async def main():

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

    # Use the lusid_scheduler ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ImagesApi)
        name = 'name_example' # str | The name and tag of the image. Format \"ExampleImageName:0.1\"

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.delete_image(name, opts=opts)

            # [EXPERIMENTAL] DeleteImage: Delete a Docker Image
            api_response = await api_instance.delete_image(name)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ImagesApi->delete_image: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name and tag of the image. Format \&quot;ExampleImageName:0.1\&quot; | 

### Return type

**str**

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

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **download_image**
> bytearray download_image(name)

[EXPERIMENTAL] DownloadImage: Download Docker Image

### Example

```python
import asyncio
from lusid_scheduler.exceptions import ApiException
from lusid_scheduler.extensions.configuration_options import ConfigurationOptions
from lusid_scheduler.models import *
from pprint import pprint
from lusid_scheduler import (
    ApiClientFactory,
    ImagesApi
)

async def main():

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

    # Use the lusid_scheduler ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ImagesApi)
        name = 'name_example' # str | The name and tag of the image of the image. Format \"ExampleImageName:latest\"

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.download_image(name, opts=opts)

            # [EXPERIMENTAL] DownloadImage: Download Docker Image
            api_response = await api_instance.download_image(name)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ImagesApi->download_image: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name and tag of the image of the image. Format \&quot;ExampleImageName:latest\&quot; | 

### Return type

**bytearray**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_image**
> Image get_image(name)

[EXPERIMENTAL] GetImage: Get metadata of a Docker Image

### Example

```python
import asyncio
from lusid_scheduler.exceptions import ApiException
from lusid_scheduler.extensions.configuration_options import ConfigurationOptions
from lusid_scheduler.models import *
from pprint import pprint
from lusid_scheduler import (
    ApiClientFactory,
    ImagesApi
)

async def main():

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

    # Use the lusid_scheduler ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ImagesApi)
        name = 'name_example' # str | The name and tag of a Docker image. Format \"ExampleImageName:latest\"

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_image(name, opts=opts)

            # [EXPERIMENTAL] GetImage: Get metadata of a Docker Image
            api_response = await api_instance.get_image(name)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ImagesApi->get_image: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name and tag of a Docker image. Format \&quot;ExampleImageName:latest\&quot; | 

### Return type

[**Image**](Image.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_images**
> ResourceListOfImageSummary list_images(name, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

[EXPERIMENTAL] ListImages: List all images under same image repository

### Example

```python
import asyncio
from lusid_scheduler.exceptions import ApiException
from lusid_scheduler.extensions.configuration_options import ConfigurationOptions
from lusid_scheduler.models import *
from pprint import pprint
from lusid_scheduler import (
    ApiClientFactory,
    ImagesApi
)

async def main():

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

    # Use the lusid_scheduler ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ImagesApi)
        name = 'name_example' # str | The name of the Repository
        page = 'page_example' # str | The pagination token to use to continue listing images from a previous call to list images.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
        sort_by = ['sort_by_example'] # List[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
        start = 56 # int | When paginating, skip this number of results. (optional)
        limit = 2000 # int | When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified. Maximum is 5000. (optional) (default to 2000)
        filter = 'filter_example' # str | Expression to filter the result set. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.list_images(name, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter, opts=opts)

            # [EXPERIMENTAL] ListImages: List all images under same image repository
            api_response = await api_instance.list_images(name, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ImagesApi->list_images: %s\n" % e)

asyncio.run(main())
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

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_repositories**
> ResourceListOfRepository list_repositories(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

[EXPERIMENTAL] ListRepositories: List all Docker image repositories

### Example

```python
import asyncio
from lusid_scheduler.exceptions import ApiException
from lusid_scheduler.extensions.configuration_options import ConfigurationOptions
from lusid_scheduler.models import *
from pprint import pprint
from lusid_scheduler import (
    ApiClientFactory,
    ImagesApi
)

async def main():

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

    # Use the lusid_scheduler ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ImagesApi)
        page = 'page_example' # str | The pagination token to use to continue listing images from a previous call to list images.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
        sort_by = ['sort_by_example'] # List[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
        start = 56 # int | When paginating, skip this number of results. (optional)
        limit = 2000 # int | When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified. Maximum is 5000. (optional) (default to 2000)
        filter = 'filter_example' # str | Expression to filter the result set. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.list_repositories(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter, opts=opts)

            # [EXPERIMENTAL] ListRepositories: List all Docker image repositories
            api_response = await api_instance.list_repositories(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ImagesApi->list_repositories: %s\n" % e)

asyncio.run(main())
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

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upload_image**
> UploadImageInstructions upload_image(upload_image_request)

[EXPERIMENTAL] UploadImage: Upload a Docker Image used for Scheduler jobs

Every image must have at least one tag. Note: your image will not be available until the returned Docker commands are executed.

### Example

```python
import asyncio
from lusid_scheduler.exceptions import ApiException
from lusid_scheduler.extensions.configuration_options import ConfigurationOptions
from lusid_scheduler.models import *
from pprint import pprint
from lusid_scheduler import (
    ApiClientFactory,
    ImagesApi
)

async def main():

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

    # Use the lusid_scheduler ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ImagesApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # upload_image_request = UploadImageRequest.from_json("")
        # upload_image_request = UploadImageRequest.from_dict({})
        upload_image_request = UploadImageRequest()

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.upload_image(upload_image_request, opts=opts)

            # [EXPERIMENTAL] UploadImage: Upload a Docker Image used for Scheduler jobs
            api_response = await api_instance.upload_image(upload_image_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ImagesApi->upload_image: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_image_request** | [**UploadImageRequest**](UploadImageRequest.md)| Request to upload image | 

### Return type

[**UploadImageInstructions**](UploadImageInstructions.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

