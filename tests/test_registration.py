import allure
from pages.registration_page import PracticeFormPage

@allure.title("Успешное заполнение формы")
def test_practice_form(browser_management):
    practice_form = PracticeFormPage()

    # Открытие и заполнение формы
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
        (practice_form.fill_address("123, Open Source Development Labs")
                     .choose_state("NCR")
                     .choose_city("Delhi"))

    with allure.step("Отправка формы регистрации"):
        practice_form.submit_button()

    with allure.step("Сравнение отправленных и переданных значений"):
        practice_form.should_registered_user_with(
            full_name="Linus Torvalds",
            email="torvalds@osdl.org",
            gender="Male",
            user_number="9876543210",
            birthdate="28 December,1969",
            subjects="Accounting, Maths",
            hobby="Reading",
            file="contact.jpg",
            address="123, Open Source Development Labs",
            location="NCR Delhi"
        )