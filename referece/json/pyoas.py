#
# pyoas.py - 
#

import json
import os
import enum
import os
import argparse


###############################################################################
# CONFIG
###############################################################################
MANAGEMENT_TEMPLATE = {
  "openapi": "2.0",
  "host": "api.bigcommerce.com",
  "basePath": "/stores/{store_hash}",
  "info": {
    "title": "BigCommerce Management API",
    "version": "",
    "description": "A collection of endpoints and resources indtended for use by back-end servers or trusted parties performing administrative operations. In General, what can accomplished in the Bigcommerce control can also be accomplished with the Management API.",
    "termsOfService": "",
    "license": {
      "name": ""
    }
  },
  "tags": [],
  "schemes": [
    "https"
  ],
  "produces": [
    "application/json"
  ],
  "consumes": [
    "application/json"
  ],
  "paths": {},
  "parameters": {},
  "definitions": {},
  "securityDefinitions": {
    "X-Auth-Client": {
      "type": "apiKey",
      "name": "X-Auth-Client",
      "in": "header"
    },
    "X-Auth-Token": {
      "type": "apiKey",
      "name": "X-Auth-Token",
      "in": "header"
    }
  },
  "security": [
    {
      "X-Auth-Client": []
    },
    {
      "X-Auth-Token": []
    }
  ],
  "responses": {},
  "x-stoplight": {
    "docs": {
      "includeDownloadLink": True
    }
  }
}

PAYMENT_TEMPLATE = {
  "openapi": "2.0",
  "info": {
    "title": "BigCommerce Payments API",
    "version": "",
    "description": "A BigCommerce API",
    "termsOfService": "",
    "license": {
      "name": ""
    }
  },
  "host": "api.bigcommerce.com",
  "basePath": "/stores/{store_hash}",
  "tags": [],
  "schemes": [
    "https"
  ],
  "produces": [
    "application/json"
  ],
  "consumes": [
    "application/json"
  ],
  "paths": {},
  "parameters": {},
  "definitions": {},
  "securityDefinitions": {
    "X-Auth-Client": {
      "type": "apiKey",
      "name": "X-Auth-Client",
      "in": "header"
    },
    "X-Auth-Token": {
      "type": "apiKey",
      "name": "X-Auth-Token",
      "in": "header"
    }
  },
  "security": [
    {
      "X-Auth-Client": []
    },
    {
      "X-Auth-Token": []
    }
  ],
  "responses": {},
  "x-stoplight": {
    "docs": {
      "includeDownloadLink": True
    }
  }
}

PROVIDER_TEMPLATE = {
  "openapi": "2.0",
  "info": {
    "title": "BigCommerce Provider API Descriptions",
    "version": "",
    "description": "A BigCommerce Provider API Descriptions are a set of API contracts intended for use by third parties wishing to integrate their service with BigCommerce.For example, the Shipping Provider API allows third parties to integrate their own shipping carriers into the BigCommerce checkout and control panel. Once integrated, shoppers can fetch quotes on the front-end from the shipping carrier within the cart and checkout pages as they do with any other shipping provider available today.",
    "termsOfService": "",
    "license": {
      "name": ""
    }
  },
  "host": "{provider_server}",
  "tags": [],
  "schemes": [
    "https"
  ],
  "produces": [
    "application/json"
  ],
  "consumes": [
    "application/json"
  ],
  "paths": {},
  "parameters": {},
  "definitions": {},
  "responses": {},
  "x-stoplight": {
    "docs": {
      "includeDownloadLink": True
    }
  }
}

STOREFRONT_TEMPLATE = {
  "openapi": "2.0",
  "info": {
    "title": "BigCommerce Storefront API",
    "version": "",
    "description": "A BigCommerce API",
    "termsOfService": "",
    "license": {
      "name": ""
    }
  },
  "host": "api.bigcommerce.com",
  "basePath": "/stores/{store_hash}",
  "tags": [],
  "schemes": [
    "https"
  ],
  "produces": [
    "application/json"
  ],
  "consumes": [
    "application/json"
  ],
  "paths": {},
  "parameters": {},
  "definitions": {},
  "securityDefinitions": {
    "X-Auth-Client": {
      "type": "apiKey",
      "name": "X-Auth-Client",
      "in": "header"
    },
    "X-Auth-Token": {
      "type": "apiKey",
      "name": "X-Auth-Token",
      "in": "header"
    }
  },
  "security": [
    {
      "X-Auth-Client": []
    },
    {
      "X-Auth-Token": []
    }
  ],
  "responses": {},
  "x-stoplight": {
    "docs": {
      "includeDownloadLink": True
    }
  }
}

PATH_TEMPLATE = {
  "openapi": "2.0",
  "info": {
    "title": "{title}",
    "description": "{description}"
  },
  "tags": [],
  "paths": {},
}

COMPONENT_TEMPLATE = {
  "openapi": "2.0",
  "info": {
    "title": "{title}",
    "description": "{description}",
  },
  "parameters": {},
  "definitions": {},
  "responses": {},
}

KEYS_TO_AGGREGATE = [
    "definitions",
    "parameters",
    "paths",
    "responses",
    "tags"
]


###############################################################################
# CODE
###############################################################################
def path_prefix(spec):
  if "basePath" not in spec.keys():
    return ""
  p = spec["basePath"].split("/")[-1]
  if p == "v3" or p == "v2" or p == "storefront":
    return "/" + p
  return ""

def is_v2(spec):
  return "basePath" in spec.keys() and "v2" in spec["basePath"]

def is_v3(spec):
  return "basePath" in spec.keys() and "v3" in spec["basePath"]

def is_payment(spec):
    return "host" in spec.keys() and "payments" in spec["host"]

def is_storefront(spec):
  return "basePath" in spec.keys() and "storefront" in spec["basePath"]
    
def is_operation(k):
  return k in [
    "post",
    "put",
    "delete",
    "get",
    "patch"
  ]

def clean_tags(spec):
  if "paths" not in spec.keys():
    return
  if len(spec["paths"].keys()) < 1:
    return
  for k,v in spec["paths"].items():
    path_tags = []
    for part in k.split("/"):
      if "{" not in part and part != "":
        path_tags.append(part)
    for kb,vb in v.items():
      if is_operation(kb):
        spec["paths"][k][kb]["tags"] = path_tags
  return spec

def get_all(key):
    """returns all values for given key in json files in current working dir"""
    aggregated_list = []
    aggregated_dict = {}
    for file in os.listdir(os.getcwd()):
        if file.endswith(".oas2.json") or file.endswith(".oas3.json"):
            with open(os.path.join(os.getcwd(), file)) as json_file:
                spec = json.load(json_file)
                spec = clean_tags(spec)
                if key in spec.keys() and type(spec[key]) == list:
                    aggregated_list.extend(spec[key])
                if key in spec.keys() and type(spec[key]) == dict:
                    for k,v in spec[key].items():
                        if key == "paths":
                          k = path_prefix(spec) + k
                        aggregated_dict[k] = v
    if type(spec[key]) == list:
        return aggregated_list
    return aggregated_dict


###############################################################################
# CLI
###############################################################################
def color(text, options):
    choices = {
        "red": '\033[95m',
        "blue": '\033[94m',
        "green": '\033[92m',
        "yellow": '\033[93m',
        "red": '\033[91m',
        "bold": '\033[1m',
        "underline": '\033[4m',
    }
    for option in options:
        text = choices[option] + text 
    return text + '\033[0m'

def get_parser():
    parser = argparse.ArgumentParser(
        prog="pyoas", 
        description="manipulates OAS files",
        epilog="...awesomely")

    parser.add_argument('--aggregate', action='store_true')
    parser.add_argument('--version', action='version', version='%(prog)s 2.0')
    return parser

if __name__ == "__main__":
    
    parser = get_parser()
    options = parser.parse_args()

    if options.aggregate:
        for key in KEYS_TO_AGGREGATE:
            MANAGEMENT_TEMPLATE[key] = get_all(key)
        print(json.dumps(MANAGEMENT_TEMPLATE))