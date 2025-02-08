import pytest
import os
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    chrome_options = Options()

    # Управление headless-режимом через переменные окружения
    if os.getenv('HEADLESS', 'false').lower() == 'true':
        chrome_options.add_argument('--headless')

    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Указываем кастомную директорию кэша через переменную окружения
    os.environ['WDM_LOCAL'] = '1'  # Использовать локальный драйвер
    os.environ['WDM_CACHE_DIR'] = '/tmp/wdm'  # Указываем папку для кэширования драйверов

    # Установка драйвера
    driver_path = ChromeDriverManager().install()

    browser.config.driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

    # Настройки Selene
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 10

    yield

    browser.quit()
