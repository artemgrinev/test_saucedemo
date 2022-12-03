import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    yield driver
    driver.quit()



