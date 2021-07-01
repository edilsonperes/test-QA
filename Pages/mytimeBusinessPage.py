from selenium import webdriver
from selenium.webdriver.common.by import By


class mytimeBusiness:
    '''Performs actions on business page.'''
    # Class variables
    service_filter_locator_type = By.XPATH
    service_filter_locator = "//section[@class='service']//span[contains(text(), '{}')]"
    staff_filter_locator_type = By.XPATH
    staff_filter_locator = "(//section[@class='staff-member']//span)[{}]"

    def __init__(self, driver) -> None:
        '''Constructor for class.'''
        self.driver = driver

    def filterService(self, service: str) -> None:
        '''Apply a filter for services.\n
        Notes:\n
        (1) You can provide just partial service name to search for.\n
        (2) Service name is case sensitive.'''
        self.driver.find_element(
            self.service_filter_locator_type, self.service_filter_locator.format(service)).click()

    def filterStaff(self, staff: int) -> None:
        '''Aplly a filter for staff considering position on the list.\n
        Note:\n
        (1) Position indexing for staff member starts from 1.\n
        (2) Position 0 = "All Staff Members".'''
        self.driver.find_element(
            self.staff_filter_locator_type, self.staff_filter_locator.format(staff+1)).click()
