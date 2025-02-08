import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    """Добавление скриншота страницы в Allure отчет."""
    png = browser.driver.get_screenshot_as_png()
    allure.attach(
        body=png,
        name='Screenshot',
        attachment_type=AttachmentType.PNG,
        extension='.png'
    )


def add_logs(browser):
    """Добавление логов консоли браузера в Allure отчет."""
    logs = browser.driver.get_log('browser')
    formatted_logs = "\n".join(f"{log['level']}: {log['message']}" for log in logs)
    allure.attach(
        body=formatted_logs,
        name='Browser Logs',
        attachment_type=AttachmentType.TEXT,
        extension='.log'
    )


def add_html(browser):
    """Добавление исходного HTML-кода страницы в Allure отчет."""
    html = browser.driver.page_source
    allure.attach(
        body=html,
        name='Page Source',
        attachment_type=AttachmentType.HTML,
        extension='.html'
    )


def add_video(browser):
    """Добавление видео выполнения теста из Selenoid в Allure отчет."""
    session_id = browser.driver.session_id
    video_url = f"https://selenoid.autotests.cloud/video/{session_id}.mp4"

    # HTML-контейнер для встраивания видео в Allure отчет
    video_html = (
        f"<html><body><video width='100%' height='100%' controls autoplay>"
        f"<source src='{video_url}' type='video/mp4'></video></body></html>"
    )

    allure.attach(
        body=video_html,
        name=f'Video_{session_id}',
        attachment_type=AttachmentType.HTML,
        extension='.html'
    )
