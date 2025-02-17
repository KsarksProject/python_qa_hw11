from pages.registration_page import PracticeFormPage
import allure
from selene import browser


@allure.title("Успешное заполнение формы")
def test_practice_form(browser_management):
    practice_form = PracticeFormPage()

    with allure.step("Открытие страницы регистрации"):
        practice_form.open()

    with allure.step("Заполнение полного имени"):
        (practice_form.fill_first_name("Linus")
                     .fill_last_name("Torvalds"))

    with allure.step("Заполнение email"):
        practice_form.fill_email("torvalds@osdl.org")

    with allure.step("Выбор пола"):
        practice_form.select_gender("Male")

    with allure.step("Заполнение номера телефона"):
        practice_form.fill_user_number("9876543210")

    with allure.step("Выбор даты рождения"):
        practice_form.pick_date_of_birth("1969", "December", "28")

    with allure.step("Выбор интересующих предметов"):
        (practice_form.fill_subject("Accounting")
                     .fill_subject("Maths"))

    with allure.step("Выбор хобби"):
        practice_form.choose_interest_reading()

    with allure.step("Добавление картинки"):
        practice_form.upload_picture("contact.jpg")

    with allure.step("Заполнение полного адреса"):
        practice_form.fill_address("123, Open Source Development Labs")

        # Удаляем все iframe перед кликом, чтобы избежать блока рекламы
        browser.execute_script("document.querySelectorAll('iframe').forEach(iframe => iframe.remove());")

        practice_form.choose_state("NCR")
        practice_form.choose_city("Delhi")

    with allure.step("Отправка формы регистрации"):
        practice_form.submit_button()

    with allure.step("Сравнение отправленных и переданных значений"):
        practice_form.should_registered_user_with(
            "Linus Torvalds",
            "torvalds@osdl.org",
            "Male",
            "9876543210",
            "28 December,1969",
            "Accounting, Maths",
            "Reading",
            "contact.jpg",
            "123, Open Source Development Labs",
            "NCR Delhi"
        )
