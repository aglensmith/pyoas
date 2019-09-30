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