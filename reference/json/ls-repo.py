import requests
import sys

[print(i["name"]) for i in requests.get('https://api.github.com/repos/{0}/contents/{1}'.format(sys.argv[1], sys.argv[2])).json()]