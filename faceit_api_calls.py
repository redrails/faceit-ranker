import http.client
import json

api_url = "open.faceit.com"
api_key = "b11d43bc-9a8c-414b-855f-3af72e620f37"

api_req_prefix = "/data/v4"

hub_id = "011b67b8-7622-4fd1-8d9c-e20e42ea6f3d"

request_types = {
    "matches": "/matches",
    "stats": "/stats"
}


def get_hub_matches(api_key, hub_id, request_type):
    connection = http.client.HTTPSConnection(api_url)
    headers = {
        'User-Agent': 'python',
        'Authorization': 'Bearer ' + api_key,
        'Content-type': 'application/json'
    }

    connection.request('GET', api_req_prefix + "/hubs/" + hub_id + request_type +"?limit=200", '', headers)
    response = connection.getresponse()
    return response.read().decode().encode('utf-8')


print(get_hub_matches(api_key, hub_id, request_types["stats"]))

