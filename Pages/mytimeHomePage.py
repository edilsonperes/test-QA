from selenium import webdriver
from selenium.webdriver.common.by import By


class mytimeSearch:
    '''Searches for a service in a city'''
    cookies_locator_type = By.ID
    cookies_locator = "accept-cookies-and-close-button"
    service_locator_type = By.XPATH
    service_locator = "(//input[@id='search-query'])[2]"
    location_locator_type = By.XPATH
    location_locator = "(//*[@id='search-location'])[2]"
    search_button_locator_type = By.XPATH
    search_button_locator = "(//button[text()='Search'])[2]"

    def __init__(self, driver) -> None:
        '''Constructor for class'''
        self.driver = driver

    def acceptCookies(self):
        '''Click the button to accept the cookies'''
        self.driver.find_element(
            self.cookies_locator_type, self.cookies_locator).click()

    def setService(self, service):
        '''Fill out the service field'''
        self.driver.find_element(
            self.service_locator_type, self.service_locator).send_keys(service)

    def setLocation(self, location):
        '''Fill out the location field'''
        self.driver.find_element(
            self.location_locator_type, self.location_locator).clear()
        self.driver.find_element(
            self.location_locator_type, self.location_locator).send_keys(location)

    def clickSearchButton(self):
        '''Clicks the search button to search for the service'''
        self.driver.find_element(
            self.search_button_locator_type, self.search_button_locator).click()