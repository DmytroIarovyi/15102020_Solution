import json
import ssl
import time
from queue import Queue

import paho.mqtt.client as mqtt
from connection_configuration.certificate import Certificate

from config import config

q = Queue()  # object for storing mqtt message
timeout = 2


def on_message(client, userdata, message):
    q.put(message)


def on_connect(client, userdata, flags, rc):
    print("----\nconnected")


class FlightUpdateListener:
    def __init__(self, topic):
        # topic to subscibe in format as described in
        # https://developer.lufthansa.com/docs/read/api_basics/notification_service/Subscribe_to_a_Topic
        self._topic = topic
        self.client = None

    def _setup_mqtt_client(self):
        cert = Certificate()
        cert.create_user_certificate_files()

        self.client = mqtt.Client('agent_001')
        self.client.on_message = on_message
        self.client.on_connect = on_connect

        print("connecting to broker\n----")
        self.client.tls_set(ca_certs=config['MQTT']['CERT_PEM_PATH'],
                            certfile=config['MQTT']['CLIENT_CERT_PATH'],
                            keyfile=config['MQTT']['PRIVATE_KEY'],
                            tls_version=ssl.PROTOCOL_TLSv1_2)

    def start_and_subscribe(self):
        self._setup_mqtt_client()
        self.client.connect(config['MQTT']['BROKER_ADDRESS'], 8883)

        print('Subscribing to topic : {topic}'.format(topic=self._topic))
        self.client.subscribe(self._topic)

        self.client.loop_start()

    def get_flight_number_data(self, amount=1):
        """
        Connect, subscribe and get Flight number data e.g.  ['LH1234']
        :param amount: Amount of Flight numbers you want to get
        :return: list of Flight numbers e.g. ['LH1234', 'LH4321']
        """
        self.start_and_subscribe()

        while q.qsize() < amount:
            # wait for message to be added to queue
            time.sleep(timeout)

        self.client.loop_stop()
        self.client.disconnect()

        result = []
        while not q.empty():
            mqtt_msg = q.get()
            as_json = json.loads(mqtt_msg.payload.decode("utf-8"))
            flight_number = as_json['Update']['FlightNumber']
            print('Flight number is: {number}'.format(number=flight_number))
            result.append(flight_number)

        return result
