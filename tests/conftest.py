from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selene import browser
import os

@pytest.fixture(scope='function')
def setup_browser():
    chrome_options = Options()

    # Включаем headless режим, если переменная окружения CI установлена в true
    if os.getenv('CI', 'false').lower() == 'true':
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Используем кастомный путь для кеша драйвера
    driver_path = ChromeDriverManager(path='/tmp/wdm').install()

    browser.config.driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)
    browser.config.base_url = 'https://demoqa.com'

    yield browser

    browser.quit()
