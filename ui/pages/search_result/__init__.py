from seleniumpagefactory.Pagefactory import PageFactory


class SearchResultPage(PageFactory):

    def __init__(self, driver):
        super(SearchResultPage, self).__init__()
        self.driver = driver

    locators = {
        'departure_scheduled_time': ('class_name', 'scheduled-time.wrap-text-sm-left'),
        'departed_actual_time': ('class_name', 'status.wrap-text-sm-left.departed'),
        'arrival_scheduled_time': ('class_name', 'scheduled-time.wrap-text-sm-right'),
        'departure_airport': ('class_name', 'airport-code'),
        'arrival_airport': ('class_name', 'airport-code.text-right')
    }

    @property
    def departure_scheduled_time_value(self):
        return self.departure_scheduled_time.find_element_by_tag_name('div').text

    @property
    def departed_actual_time_value(self):
        return self.departed_actual_time.find_element_by_class_name('best-time').text

    @property
    def arrival_scheduled_time_value(self):
        return self.arrival_scheduled_time.find_element_by_class_name('best-time').text

    @property
    def arrival_actual_time_value(self):
        return self.driver.find_elements_by_class_name('best-time')[1].text

    def get_airport_by_locator(self, locator):
        """
        Get and combine airport data
        :param locator: WebElement to search in
        :return: str, e.g. 'TXL Berlin'
        """
        abbr = locator.find_element_by_tag_name('span').text
        city = locator.find_element_by_tag_name('p').text
        return '{abbr} {city}'.format(abbr=abbr, city=city)

    @property
    def departure_airport_value(self):
        return self.get_airport_by_locator(self.departure_airport)

    @property
    def arrival_airport_value(self):
        return self.get_airport_by_locator(self.arrival_airport)

    @property
    def status(self):
        parent = self.driver.find_elements_by_class_name('best-time')[1].find_element_by_xpath('..')
        return parent.find_element_by_tag_name('span').text
