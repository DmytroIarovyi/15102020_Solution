from seleniumpagefactory.Pagefactory import PageFactory
import datetime

from ui.pages.search_result import SearchResultPage


class TimetableAndFlightStatusPage(PageFactory):

    def __init__(self, driver):
        super(TimetableAndFlightStatusPage, self).__init__()
        self.driver = driver

    locators = {
        'flight_number_input_field': ('name', 'flightStatusByFlightNumberRequest.flightNumber'),
        # rest of used locators on this page are dynamic
    }

    def select_flight_number_tab(self):
        container = self.driver.find_element_by_class_name('tab-links')
        flight_number_button = container.find_elements_by_tag_name('a')[0]
        flight_number_button.click()

    def open_airline_dropdown(self):
        container = self.driver.find_element_by_class_name('col-5.col-md-4')
        container.find_elements_by_tag_name('button')[0].click()

    def select_airline(self, airline):
        """
        Select Airline from dropdown
        :param airline: str, e.g. 'LH'
        """
        self.open_airline_dropdown()
        container = [el for el in self.driver.find_elements_by_class_name('selectable-result-list')
                     if el.is_displayed()][0]
        elements = container.find_elements_by_class_name('sel-item')
        correct_option = [el for el in elements if el.text == airline][0]
        correct_option.click()

    def enter_flight_number(self, flight_number):
        """
        Enter Flight Number into corresponding text field
        :param flight_number: str, e.g. '1234'
        """
        self.flight_number_input_field.set_text(flight_number)

    def open_date_dropdown(self):
        container = [el for el in self.driver.find_elements_by_class_name('selectable')
                     if el.text.startswith('Date')][0]
        container.find_element_by_tag_name('button').click()

    @property
    def current_date(self):
        return datetime.datetime.today().strftime('%a %d.%m.%Y')

    def select_date(self, today, date=current_date):
        """
        Select date from dates list
        :param today: bool, Default value will be used (default = today) if True
        :param date: str, format - e.g. Tue 13.10.2020. Date to be selected in the list of dates
        """
        if today:
            return
        self.open_date_dropdown()
        container = [el for el in self.driver.find_elements_by_class_name('selectable-result-list')
                     if el.is_displayed()][0]
        elements = container.find_elements_by_tag_name('li')
        correct_option = [el for el in elements if el.text == date][0]
        correct_option.click()

    def click_search_button(self):
        container = self.driver.find_element_by_class_name('mt-7')
        container.find_element_by_tag_name('button').click()

    def search_for_flight_today(self, airline, flight_number, today=True):
        """
        Search for today's flight
        :param airline: str, e.g. 'LH'
        :param flight_number: str, e.g. '1234'
        :param today: bool, True
        :return: SearchResultPage obj
        """
        self.select_flight_number_tab()
        self.select_airline(airline)
        self.enter_flight_number(flight_number)
        self.select_date(today)
        self.click_search_button()
        return SearchResultPage(self.driver)
