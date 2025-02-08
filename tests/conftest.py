import pytest
import os
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def setup_browser():
    """Фикстура для настройки браузера с проверкой переменной CI"""

    chrome_options = Options()

    # Проверка переменной окружения CI для активации headless режима
    if os.getenv('CI', 'false').lower() == 'true':
        chrome_options.add_argument('--headless')  # Включаем headless режим в CI
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    browser.config.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 10

    yield browser

    browser.quit()
