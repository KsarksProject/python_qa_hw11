import pytest
import os
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    """Фикстура для настройки браузера и управления тестами."""
    chrome_options = Options()

    # Управление headless-режимом через переменные окружения
    if os.getenv('HEADLESS', 'false').lower() == 'true':
        chrome_options.add_argument('--headless')

    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Автоматическая установка ChromeDriver через webdriver-manager
    browser.config.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    # Основные настройки браузера
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 10  # Таймаут ожидания элементов

    yield  # Выполнение теста

    # Закрытие браузера после выполнения теста
    browser.quit()
