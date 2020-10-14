from enum import Enum
import requests

from connection_configuration import certificate


class RequestType(Enum):
    GET = 1
    POST = 2


def make_request(url, request_type=RequestType.GET, return_as_json=False):
    """
    Execute request
    :param url: request url
    :param request_type: get or post (can be extended if needed)
    :param return_as_json: if True returns response in json format
    :return: response in json format or not
    """
    auth = certificate.Auth()
    header = auth.get_header()

    r = requests.post(url, headers=header) if request_type == RequestType.POST else requests.get(url, headers=header)
    if r.status_code == 200:
        return r.json() if return_as_json else r.text
    else:
        return '{code} {reason}'.format(code=r.status_code, reason=r.reason)
