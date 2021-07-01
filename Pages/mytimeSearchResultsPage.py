from selenium import webdriver
from selenium.webdriver.common.by import By


class mytimeResults:
    '''Executes actions on search results page.'''
    # Class variables
    results_locator_type = By.XPATH
    results_locator = "//ul[@id='results']/li"
    business_locator_type = By.XPATH
    business_locator = "//ul[@id='results']//a[contains(text(),'{}')]"

    def __init__(self, driver) -> None:
        '''Constructor for class.'''
        self.driver = driver

    def countResults(self) -> int:
        '''Counts how many results are shown to the user.'''
        results = self.driver.find_elements(
            self.results_locator_type, self.results_locator)
        return len(results)

    def selectBusiness(self, business_name: str) -> None:
        '''Selects the business that matches the business name.\n
        Notes:\n
        (1) You can provide just partial business name to search for.\n
        (2) Business name is case sensitive.'''
        self.driver.find_element(
            self.business_locator_type, self.business_locator.format(business_name)).click()
