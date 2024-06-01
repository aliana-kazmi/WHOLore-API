import requests
from urllib.parse import unquote
endpoint = "https://www.google.com/"

get_response = requests.get(
    endpoint
    )
try:

    a=get_response
    print(a)
except:
    print('empty inside')
