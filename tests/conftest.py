from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    chrome_options = Options()

    # Управляем режимом headless через переменные окружения
    if os.getenv('HEADLESS', 'false').lower() == 'true':
        chrome_options.add_argument('--headless')

    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Указываем кастомную папку для кэширования драйвера
    driver_path = ChromeDriverManager(path="/tmp/wdm").install()

    browser.config.driver = webdriver.Chrome(
        service=Service(driver_path),
        options=chrome_options
    )

    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 10

    yield
    browser.quit()
