import os
import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType


@pytest.fixture(scope="function")
def setup_browser():
    """Фикстура для настройки браузера с Allure аттачами."""

    options = Options()
    options.add_argument('--window-size=1920,1080')

    # Проверка на использование Selenoid или локального запуска
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    if login and password:
        # Удалённое подключение через Selenoid
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "126.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options.capabilities.update(selenoid_capabilities)
        driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
            options=options
        )
    else:
        # Локальный запуск браузера
        driver = webdriver.Chrome(options=options)

    browser.config.driver = driver
    browser.config.base_url = 'https://demoqa.com'
    yield browser

    # Добавление аттачей после выполнения теста
    attach_allure_artifacts(browser)

    browser.quit()


def attach_allure_artifacts(browser):
    """Добавление скриншотов, исходного кода страницы, логов и видео в Allure."""
    if hasattr(browser, 'driver'):
        try:
            # Скриншот страницы
            allure.attach(
                browser.driver.get_screenshot_as_png(),
                name='Скриншот страницы',
                attachment_type=AttachmentType.PNG
            )

            # Исходный код страницы
            allure.attach(
                browser.driver.page_source,
                name='Исходный код страницы',
                attachment_type=AttachmentType.HTML
            )

            # Логи консоли браузера
            logs = browser.driver.get_log('browser')
            logs_text = "\n".join([f"{log['level']}: {log['message']}" for log in logs])
            allure.attach(
                logs_text,
                name='Логи консоли',
                attachment_type=AttachmentType.TEXT
            )

            # Видео (только для Selenoid)
            session_id = browser.driver.session_id
            video_url = f"https://selenoid.autotests.cloud/video/{session_id}.mp4"
            allure.attach(
                f"<html><body><video width='100%' height='100%' controls autoplay>"
                f"<source src='{video_url}' type='video/mp4'></video></body></html>",
                name='Видео выполнения теста',
                attachment_type=AttachmentType.HTML
            )

        except Exception as e:
            allure.attach(
                str(e),
                name='Ошибка при добавлении аттачей',
                attachment_type=AttachmentType.TEXT
            )
