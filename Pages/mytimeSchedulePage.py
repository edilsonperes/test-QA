from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class mytimeSchedule:
    '''Performs actions on schedule page.'''
    # Class variables
    available_times_locator_type = By.XPATH
    available_times_locator = "//h5"
    next_day_locator_type = By.XPATH
    next_day_locator = "(//div[@class[contains(.,'today')]]/../../following-sibling::button[1]//div)[2]"
    next_week_locator_type = By.XPATH
    next_week_locator = "//div[@class[contains(.,'NextWeekArrow')]]"
    service_name_locator_type = By.XPATH
    service_name_locator = "//li//div[@class='col-left']/span"
    service_price_locator_type = By.XPATH
    service_price_locator = "//li//div[@class='col-right']//span[@class='normal-price']"
    staff_name_locator_type = By.XPATH
    staff_name_locator = "//td[contains(text(),'booking with')]/..//span[@class='Select-value-label']"

    def __init__(self, driver) -> None:
        '''Constructor for class.'''
        self.driver = driver

    def countAvailableTimes(self) -> int:
        '''Counts available times for scheduling.'''
        try:
            self.driver.find_element(
                self.available_times_locator_type, self.available_times_locator)
        except NoSuchElementException:
            try:
                self.driver.find_element(
                    self.next_day_locator_type, self.next_day_locator).click()
            except NoSuchElementException:
                self.driver.find_element(
                    self.next_week_locator_type, self.next_week_locator).click()

        return len(self.driver.find_elements(self.available_times_locator_type, self.available_times_locator))

    def getServiceName(self) -> str:
        '''Gets the service name.'''
        return self.driver.find_element(self.service_name_locator_type, self.service_name_locator).text

    def getServicePrice(self) -> str:
        '''Gets the service price.'''
        return self.driver.find_element(self.service_price_locator_type, self.service_price_locator).text

    def getStaffName(self) -> str:
        '''Gets the staff name.'''
        return self.driver.find_element(self.staff_name_locator_type, self.staff_name_locator).text
