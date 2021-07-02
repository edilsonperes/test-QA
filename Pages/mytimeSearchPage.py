from selenium.webdriver.common.by import By


class mytimeSearch:
    '''Performs actions on search page.'''
    # Class variables
    service_locator_type = By.XPATH
    service_locator = "(//input[@id='search-query'])[2]"
    location_locator_type = By.XPATH
    location_locator = "(//*[@id='search-location'])[2]"
    search_button_locator_type = By.XPATH
    search_button_locator = "(//button[text()='Search'])[2]"

    def __init__(self, driver) -> None:
        '''Constructor for class.'''
        self.driver = driver

    def setService(self, service: str) -> None:
        '''Fill out the service field.'''
        self.driver.find_element(
            self.service_locator_type, self.service_locator).send_keys(service)

    def setLocation(self, location: str) -> None:
        '''Fill out the location field.'''
        self.driver.find_element(
            self.location_locator_type, self.location_locator).clear()
        self.driver.find_element(
            self.location_locator_type, self.location_locator).send_keys(location)

    def clickSearchButton(self) -> None:
        '''Clicks the search button.'''
        self.driver.find_element(
            self.search_button_locator_type, self.search_button_locator).click()

    def searchService(self, service: str, location: str) -> None:
        '''Searches for the service in the location.'''
        self.setService(service)
        self.setLocation(location)
        self.clickSearchButton()
