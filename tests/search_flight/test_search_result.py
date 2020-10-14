import pytest


@pytest.fixture(scope='module')
def departure_times(search_result_page):
    return {'exp_time': search_result_page.departure_scheduled_time_value,
            'act_time': search_result_page.departed_actual_time_value}


@pytest.fixture(scope='module')
def arrival_times(search_result_page):
    return {'exp_time': search_result_page.arrival_scheduled_time_value,
            'act_time': search_result_page.arrival_actual_time_value}


def test_departure_or_arrival_time_is_different(departure_times, arrival_times):
    assert departure_times['exp_time'] != departure_times['act_time'] or arrival_times[
        'exp_time'] != arrival_times['act_time'], \
        'Actual Departure or Arrival time should be different than Scheduled'


def test_write_flight_data(search_result_page):
    departing_airport = search_result_page.departure_airport_value
    arriving_airport = search_result_page.arrival_airport_value
    dep_time = search_result_page.departed_actual_time_value
    arr_time = search_result_page.arrival_actual_time_value
    status = search_result_page.status

    print(' .... {} - {} - {} - {} - {}'.format(departing_airport, arriving_airport, dep_time, arr_time, status))
