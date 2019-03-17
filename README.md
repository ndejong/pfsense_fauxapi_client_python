# PfsenseFauxapi - Python Interface

[![PyPi](https://img.shields.io/pypi/v/pfsense-fauxapi.svg)](https://pypi.org/project/pfsense-fauxapi/)
[![Build Status](https://travis-ci.org/ndejong/pfsense_fauxapi_client_python.svg?branch=master)](https://travis-ci.org/ndejong/pfsense_fauxapi_client_python)

Python client for pfSense-FauxAPI - https://github.com/ndejong/pfsense_fauxapi

Available as a PyPi package, to install, installs an API _client_ for to interact with a 
pfSense host that has the FauxAPI package installed.   
```bash
pip3 install pfsense-fauxapi
```

### Code Examples
Three Python code samples are provided that demonstrate interface usage

* `function-iterate.py` - iterates (almost) all the FauxAPI functions to confirm operation.  
* `update-aws-aliases.py` - downloads the latest AWS `ip-ranges.json` and populates the pfsense alias table(s).
* `usergroup-management.py` - demonstrates the ability to manage users and groups programmatically. 


### Command Line
Additionally this pip-package provides a command-line interface to work with FauxAPI
```bash
usage: fauxapi [-h] [--host [host]] [--apikey [key]] [--apisecret [secret]]
               [--verified-ssl] [--debug]
               [function] [[function] ...] [[function-args]]

FauxAPI

optional arguments:
  -h, --help            show this help message and exit

Call:
  --host [host]         Host address of the target pfSense host with the
                        PfsenseFauxapi package installed.
  --apikey [key]        FauxAPI apikey value - alternatively via the
                        FAUXAPI_APIKEY environment variable.
  --apisecret [secret]  FauxAPI apisecret value - alternatively via the
                        FAUXAPI_APIKEY environment variable.
  --verified-ssl        Enable SSL certificate checks - default does NOT check
                        SSL certificates.
  --debug               Enable debug response from the remote FauxAPI -
                        helpful in tracking down issues.
  [function]            The FauxAPI function being called
  [function-args]       Arguments to the function, space separated
```

Command line example, using environment variables to pass the `FAUXAPI_APIKEY` 
and `FAUXAPI_APIKEY` credentials.
```bash
$ fauxapi --host 192.168.1.200 gateway_status | jq .
{
  "callid": "5c8d0f7361cba",
  "action": "gateway_status",
  "message": "ok",
  "data": {
    "gateway_status": {
      "10.11.12.1": {
        "monitorip": "10.10.10.1",
        "srcip": "10.10.10.200",
        "name": "WAN_DHCP",
        "delay": "0.422ms",
        "stddev": "0.073ms",
        "loss": "0.0%",
        "status": "none"
      }
    }
  }
}
```

### Package Testing
Tests for (almost) all client-side function calls are implemented with mocked API response data
you can check them with pytest
```bash
python3 setup.py test
```

Packages are tested via Travis
[travis-ci.org/ndejong/pfsense_fauxapi_client_python](https://travis-ci.org/ndejong/pfsense_fauxapi_client_python)

### Package Build
Should you need/want to build the package from source
```bash
# obtain the source material
git clone https://github.com/ndejong/pfsense_fauxapi_client_python.git
cd pfsense_fauxapi_client_python

# build the package
python3 setup.py sdist bdist_wheel

# install the package from the .whl file in the dist path 
pip install dist/pfsense*.whl
```
