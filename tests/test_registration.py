import allure
from allure_commons.types import Severity
from pages.registration_page import RegistrationPage
from models.user import User


@allure.tag('web')
@allure.feature("Practice form")
@allure.story("Проверка регистрации")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Aleksandr Bardashevich")
@allure.description("Тест проверяет регистрацию")
@allure.link("https://demoqa.com", name="demoqa.com")
def test_registration_form(browser_management):
    user = User(
        first_name='Linus',
        last_name='Torvalds',
        email='torvalds@osdl.org',
        gender='Male',
        mobile='9876543210',
        birth_day='28',
        birth_month='December',
        birth_year='1969',
        subjects=['Accounting', 'Maths'],
        hobby='Reading',
        picture='contact.jpg',
        address='123, Open Source Development Labs',
        state='NCR',
        city='Delhi'
    )

    expected_results = {
        'Student Name': f"{user.first_name} {user.last_name}",
        'Student Email': user.email,
        'Gender': user.gender,
        'Mobile': user.mobile,
        'Date of Birth': f"{user.birth_day} {user.birth_month},{user.birth_year}",
        'Subjects': ', '.join(user.subjects),
        'Hobbies': user.hobby,
        'Picture': user.picture,
        'Address': user.address,
        'State and City': f"{user.state} {user.city}"
    }

    registration_page = RegistrationPage()

    with allure.step("Открываем страницу регистрации"):
        registration_page.open()

    with allure.step("Заполняем форму регистрации и отправляем данные"):
        registration_page.register(user)

    with allure.step("Проверяем, что данные регистрации отображаются корректно"):
        registration_page.should_have_registered(expected_results)
