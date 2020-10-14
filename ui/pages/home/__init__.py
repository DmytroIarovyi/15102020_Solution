from seleniumpagefactory.Pagefactory import PageFactory

from config import config
from ui.pages.timetable_and_flight_status import TimetableAndFlightStatusPage


class HomePage(PageFactory):

    def __init__(self, driver):
        super(HomePage, self).__init__()
        self.driver = driver
        self.timeout = int(config['TIMEOUT']['DRIVER'])

    locators = {
        'agree_button': ('id', 'cm-acceptAll'),
        'menu_button': ('id', 'nav'),
        'flight_status_button': ('xpath', '//*[@id="list-3"]/li[7]/a')
    }

    def accept_cookies(self):
        self.agree_button.click_button()

    def open_menu(self):
        self.menu_button.click_button()

    def open_timetable_and_flight_status(self):
        self.accept_cookies()
        self.open_menu()
        self.flight_status_button.click_button()
        return TimetableAndFlightStatusPage(self.driver)
