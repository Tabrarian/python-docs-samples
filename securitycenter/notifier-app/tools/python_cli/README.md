# api_client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import api_client
from api_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: google_id_token
api_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: google_id_token_https
api_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# create an instance of the API class
api_instance = api_client.DefaultApi()
body = api_client.ChannelsRequestBody() # ChannelsRequestBody |  (optional)

try:
    api_instance.gcp_noti_api_channels(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->gcp_noti_api_channels: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://$API_ENDPOINT_URL/_ah/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**gcp_noti_api_channels**](docs/DefaultApi.md#gcp_noti_api_channels) | **POST** /gcpNotiApi/v1/channels | 
*DefaultApi* | [**gcp_noti_api_config**](docs/DefaultApi.md#gcp_noti_api_config) | **POST** /gcpNotiApi/v1/config | 
*DefaultApi* | [**gcp_noti_api_rules**](docs/DefaultApi.md#gcp_noti_api_rules) | **POST** /gcpNotiApi/v1/rules | 
*DefaultApi* | [**gcp_noti_api_set_extra_info**](docs/DefaultApi.md#gcp_noti_api_set_extra_info) | **POST** /gcpNotiApi/v1/extrainfo | 
*DefaultApi* | [**gcp_noti_api_set_status**](docs/DefaultApi.md#gcp_noti_api_set_status) | **POST** /gcpNotiApi/v1/status | 
*DefaultApi* | [**gcp_noti_api_users**](docs/DefaultApi.md#gcp_noti_api_users) | **POST** /gcpNotiApi/v1/users | 


## Documentation For Models

 - [Action](docs/Action.md)
 - [ApiUser](docs/ApiUser.md)
 - [ChannelRequest](docs/ChannelRequest.md)
 - [ChannelsRequestBody](docs/ChannelsRequestBody.md)
 - [ConfigurationRequestBody](docs/ConfigurationRequestBody.md)
 - [ExtraInfoRequestBody](docs/ExtraInfoRequestBody.md)
 - [Rule](docs/Rule.md)
 - [RulesRequestBody](docs/RulesRequestBody.md)
 - [StatusRequest](docs/StatusRequest.md)
 - [UsersRequestBody](docs/UsersRequestBody.md)


## Documentation For Authorization


## google_id_token

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: 
- **Scopes**: N/A

## google_id_token_https

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: 
- **Scopes**: N/A


## Author



