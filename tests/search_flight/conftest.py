import pytest


@pytest.fixture(scope='module')
def timetable_and_flight_status_page(home_page):
    return home_page.open_timetable_and_flight_status()


@pytest.fixture(scope='module')
def search_for_flight_today(timetable_and_flight_status_page):
    def func(airline, flight_number):
        return timetable_and_flight_status_page.search_for_flight_today(airline, flight_number, today=True)

    return func


@pytest.fixture(scope='module')
def search_result_page(airline, flight_number_wo_airline, search_for_flight_today):
    search_results_page = search_for_flight_today(airline, flight_number_wo_airline)
    return search_results_page
