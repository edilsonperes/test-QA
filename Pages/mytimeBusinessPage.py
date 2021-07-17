from selenium.webdriver.common.by import By


class mytimeBusiness:
    '''Performs actions on business page.'''
    # Class variables
    service_filter_locator_type = By.XPATH
    service_filter_locator = "//section[@class='service']//span[contains(text(), '{}')]"
    staff_filter_locator_type = By.XPATH
    staff_filter_locator = "(//section[@class='staff-member']//span)[{}]"
    service_name_locator_type = By.XPATH
    service_name_locator = "//h5/span[contains(text()," + \
        '"' + "{}" + '"' + ")]"
    service_div_locator = service_name_locator + "/../../.."
    service_price_locator_type = By.XPATH
    service_price_locator = service_div_locator + \
        "//span[contains(text(),'$')]"
    book_button_locator_type = By.XPATH
    book_button_locator = service_div_locator + "//button"
    select_time_button_locator_type = By.XPATH
    select_time_button_locator = "//div[@class='panel modal-container']//button[text()='Select Time']"

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

    def filterStaff(self, staff: int) -> str:
        '''Aplly a filter for staff considering position on the list.\n
        Note:\n
        (1) Position for staff member starts from 1.\n
        (2) Psition 0 = "All Staff Members".'''
        staff_name = self.driver.find_element(
            self.staff_filter_locator_type, self.staff_filter_locator.format(staff+1))
        staff_name.click()
        return staff_name.text

    def clickBookButton(self, service: str) -> tuple:
        '''Clicks the "Book" button for the selected service.\n
        Notes:\n
        (1) You can provide just partial service name to search for.\n
        (2) Service name is case sensitive.'''
        service_name = self.driver.find_element(
            self.service_name_locator_type, self.service_name_locator.format(service)).text
        service_price = self.driver.find_element(
            self.service_price_locator_type, self.service_price_locator.format(service)).text
        self.driver.find_element(
            self.book_button_locator_type, self.book_button_locator.format(service)).click()
        return service_name, service_price

    def clickSelectTimeButton(self) -> None:
        '''Clicks the "Select Time" button in the add-on modal opened.'''
        self.driver.find_element(
            self.select_time_button_locator_type, self.select_time_button_locator).click()
