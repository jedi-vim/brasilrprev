import json

import requests

from brprev_cli.settings import settings


def _transform_data(search_data):
    retval = dict()
    retval['keywords'] = search_data['keywords']
    retval['created_at'] = search_data['created_at'].isoformat()
    retval['result'] = dict(items=[])
    for elem in search_data['result']['items']:
        sanitazed_elem = elem.copy()
        sanitazed_elem['body'] = json.dumps(elem['body'])
        retval['result']['items'].append(sanitazed_elem)
    return retval


def broadcast_search_result(search_data):
    request_data = _transform_data(search_data)
    response = requests.post(
        f'http://{settings.BRPREV_WEB}/api/v1/search_result/broadcast',
        data=request_data)
    print(response.content)
    response.raise_for_status()
