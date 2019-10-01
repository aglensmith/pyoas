## PyOAS

Collections for python scripts for working with Open API Specification (OAS) files

## Contents
1. `combine_definitions.py` - combines the definitions for all specification files in current directory into a single json object
2. `combine_paths.py` - combines the definitions for all specification files in current directory into a single json object
3. `combine_tags.py` - combine tags
4. `combine_responses.py` - combine responses
5. `combine_parameters.py` - combine parameters

## TODO
* Combine these files into a single module
* Create a function that runs all of them called `aggregate` or something

## Hosts and basePaths

* `payments.bigcommerce.com/stores/{store_hash}`
* `api.bigcommerce.com/stores/{store_hash}/v2`
* `api.bigcommerce.com/stores/{store_hash}/v3`
* `{store_domain}/api/storefront`
* `{provider_server_domain}`
* Create the payment token: `https://api.bigcommerce.com/stores/{store_hash}/v3/payments/access_tokens`
* Process the payment:  `https://payments.bigcommerce.com/stores/{store_hash}/payments`

## Convert Swagger 2.0 to OAS 3.0

```bash
npm install -g swagger2openapi

swagger2openapi --patch https://raw.githubusercontent.com/bigcommerce/dev-docs/master/reference/json/BigCommerce_Orders_API.oas2.json
```

## Renaming Files:

```bash
# just echo to see preview
for i in *.oas2.json; do echo ${i/%.oas2.json/.oas3.json}; done

# actaual

for i in *.oas2.json; do swagger2openapi --patch $i >> oas3/${i/%.oas2.json/.oas3.json}; done
```

## Servers

The global servers array can be overridden on the path level or operation level. This is handy if some endpoints use a different server or base path than the rest of the API. Common examples are:
* Different base URL for file upload and download operations,
* Deprecated but still functional endpoints.

```yaml
servers:
  - url: https://api.example.com/v1
paths:
  /files:
    description: File upload and download operations
    servers:
      - url: https://files.example.com
        description: Override base path for all operations with the /files path
    ...
  /ping:
    get:
      servers:
        - url: https://echo.example.com
          description: Override base path for the GET /ping operation
```

## Open in Studio
```js
x = window.location.href.split("https://github.com/")[1].split("/")
window.open("https://stoplight.io/p/studio/gh/" + x[0] + "/" + x[1])
```