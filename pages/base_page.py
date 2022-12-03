from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from selenium.common.exceptions import StaleElementReferenceException


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 5)
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator) -> WebElement:
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def element_are_visible(self, locator) -> List[WebElement]:
        return self.__wait.until(EC.visibility_of_all_elements_located(locator))