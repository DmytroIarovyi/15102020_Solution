import requests

from config import config
from request import make_request, RequestType


class Auth:
    token_url = config['APP']['BASE_URL'] + 'oauth/token'

    def __init__(self):
        self._token = self.get_token()
        self._header = self.get_header()

    def get_token(self):
        data = {
            "client_id": config['AUTH']['CLIENT_ID'],
            "client_secret": config['AUTH']['CLIENT_SECRET'],
            "grant_type": "client_credentials"
        }
        r = requests.post(self.token_url, data)
        return r.json()['access_token']

    def get_header(self):
        headers = {'Accept': 'application/json', 'Authorization': 'Bearer ' + self.token}
        return headers

    @property
    def token(self):
        return self._token

    @property
    def header(self):
        return self._header


class Certificate:
    cert_url = config['APP']['BASE_URL'] + 'notifications/certificates'

    def __init__(self):
        self.__cert_data = self.certificate_data
        self._client_certificate = self.__cert_data['certificatePem']
        self._public_key = self.__cert_data['keyPair']['PublicKey']
        self._private_key = self.__cert_data['keyPair']['PrivateKey']

    def get_cert_data(self):
        json_data = make_request(url=self.cert_url, request_type=RequestType.POST, return_as_json=True)
        return json_data['CertificateManagementResource']['CertificateManagement']

    @property
    def certificate_data(self):
        return self.get_cert_data()

    def create_file(self, path_to_file, data):
        with open(path_to_file, 'w+') as file:
            file.write(data)

    def create_user_certificate_files(self):
        base_path = '../resources/mqtt_broker/'
        self.create_file(base_path + 'clientCertificate.cer', self._client_certificate)
        self.create_file(base_path + 'PrivateKey.key', self._private_key)
        self.create_file(base_path + 'PublicKey.key', self._public_key)
