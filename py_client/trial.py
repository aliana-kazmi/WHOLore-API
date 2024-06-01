import requests
from urllib.parse import unquote
endpoint = "http://127.0.0.1:3000/api/gadget/add-gadget/"

get_response = requests.post(
    endpoint,
    json={
        'name':'Super Phone', 
        'description':"A normal mobile phone modified by the Doctor's sonic screwdriver so that it can call anyone from any era of time. Used by the likes of Martha and Donna, Rose was the first companion to have her Nokia 3200 significantly upgraded, being able to ring up her mum from millions of years in the future, while watching the earth burn up in front of her.",
        'debue_date':'2005-04-02'
        })

# print(get_response.json())
try:

    a=get_response.json()
    print(a)
except:
    print('empty inside')
