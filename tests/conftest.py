import pytest
from selene import browser
import allure


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 10

    with allure.step('Открытие браузера и настройка'):
        allure.attach(
            name='Base URL',
            body=browser.config.base_url,
            attachment_type=allure.attachment_type.TEXT
        )

    yield

    # Добавление артефактов после выполнения теста
    attach_allure_artifacts()

    with allure.step('Закрытие браузера'):
        browser.quit()


def attach_allure_artifacts():
    """Добавление скриншотов, исходного кода страницы и логов консоли в Allure."""
    if hasattr(browser, 'driver'):
        try:
            # Скриншот страницы
            allure.attach(
                browser.driver.get_screenshot_as_png(),
                name='Скриншот страницы',
                attachment_type=allure.attachment_type.PNG
            )

            # Исходный код страницы
            allure.attach(
                browser.driver.page_source,
                name='Исходный код страницы',
                attachment_type=allure.attachment_type.HTML
            )

            # Логи браузера
            logs = browser.driver.get_log('browser')
            logs_text = "\n".join([f"{log['level']}: {log['message']}" for log in logs])
            allure.attach(
                logs_text,
                name='Логи консоли',
                attachment_type=allure.attachment_type.TEXT
            )

        except Exception as e:
            allure.attach(
                str(e),
                name='Ошибка при добавлении артефактов',
                attachment_type=allure.attachment_type.TEXT
            )
