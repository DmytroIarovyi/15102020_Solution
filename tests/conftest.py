import pytest

from ui.driver import Driver
from connection_configuration.mqtt_broker import FlightUpdateListener
from ui.helpers.flight_data import get_airline, get_flight_number_without_airline
from ui.pages.home import HomePage
from ui.helpers.topic import current_date


@pytest.fixture(scope='module')
def driver():
    return Driver.chrome


@pytest.fixture(scope='module')
def home_page(driver):
    return HomePage(driver)


@pytest.fixture(scope='module')
def flight_update_listener():
    topic = 'prd/FlightUpdate/LH/{date}/#'.format(date=current_date)
    return FlightUpdateListener(topic)


@pytest.fixture(scope='module', autouse=True)
def flight_number_data(flight_update_listener):
    return flight_update_listener.get_flight_number_data(amount=1)[0]


@pytest.fixture(scope='module')
def airline(flight_number_data):
    return get_airline(flight_number_data)


@pytest.fixture(scope='module')
def flight_number_wo_airline(flight_number_data):
    return get_flight_number_without_airline(flight_number_data)
