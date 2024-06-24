![LUSID_by_Finbourne](./resources/Finbourne_Logo_Teal.svg)

# LUSID<sup>®</sup> Scheduler Python SDK
This is the Python SDK for the Scheduler API for [LUSID by FINBOURNE](https://www.finbourne.com/lusid-technology), a bi-temporal investment management data platform with portfolio accounting capabilities. To use it you'll need a LUSID account. [Sign up for free at lusid.com](https://www.lusid.com/app/signup)

| branch | status |
| --- | --- |
| `main` |  ![PyPI](https://img.shields.io/pypi/v/lusid-scheduler-sdk?color=blue)

## Installation

The PyPi package for the LUSID Scheduler SDK can installed using the following:

```
pip install lusid-scheduler-sdk finbourne-sdk-utilities
```

## Usage

```
import lusid_scheduler
from fbnsdkutilities import ApiClientFactory

scheduler_factory = ApiClientFactory(lusid_scheduler, api_secrets_filename="/path/to/secrets.json")
jobs_api = scheduler_factory.build(lusid_scheduler.api.JobsApi)

jobs_api.list_jobs()
```
