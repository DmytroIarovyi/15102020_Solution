import re


def get_flight_number_without_airline(flight_number_data):
    """
    Get only flight number without airline
    :param flight_number_data: Airline+Flight number (e.g. 'LH1234')
    :return: str, e.g. '1234'
    """
    return re.findall('\d+', flight_number_data)[0]


def get_airline(flight_number_data):
    """
    Get only airline without flight number
    :param flight_number_data: Airline+Flight number (e.g. 'LH1234')
    :return: str, e.g. 'LH'
    """
    return ''.join(re.findall('[a-zA-Z]+', flight_number_data))
