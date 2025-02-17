from pages.registration_page import PracticeFormPage
import allure


@allure.title("Успешное заполнение формы")
def test_practice_form(browser_set):

    with allure.step("Открытие формы регистрации"):
        practice_form_page = PracticeFormPage()
        practice_form_page.open()

    with allure.step("Заполнение полного имени"):
        practice_form_page.fill_first_name("Linus")
        practice_form_page.fill_last_name("Torvalds")

    with allure.step("Заполнение email"):
        practice_form_page.fill_email("torvalds@osdl.org")

    with allure.step("Выбор пола"):
        practice_form_page.select_gender("Male")

    with allure.step("Заполнение номера телефона"):
        practice_form_page.fill_user_number("9876543210")

    with allure.step("Выбор даты рождения"):
        practice_form_page.pick_date_of_birth("1969", "December", "28")

    with allure.step("Выбор интересующих предметов"):
        practice_form_page.fill_subject("Accounting")
        practice_form_page.fill_subject("Maths")

    with allure.step("Выбор хобби"):
        practice_form_page.choose_interest_reading()

    with allure.step("Добавление картинки"):
        practice_form_page.upload_picture("contact.jpg")

    with allure.step("Заполнение полного адреса"):
        practice_form_page.fill_address("123, Open Source Development Labs")
        practice_form_page.choose_state("NCR")
        practice_form_page.choose_city("Delhi")

    with allure.step("Отправка формы регистрации"):
        practice_form_page.submit_button()

    with allure.step("Сравнение отправленных и переданных значений"):
        practice_form_page.should_registered_user_with(
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
