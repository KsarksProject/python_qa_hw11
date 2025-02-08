import pytest
import allure
from tests.pages.registration_page import RegistrationPage
from tests.models.user import User


@allure.epic('DemoQA Registration')
@allure.feature('User Registration Form')
@allure.story('Successful Registration with Valid Data')
@allure.label("owner", "Aleksandr Bardashevich")
@allure.tag('positive', 'regression')
@allure.severity(allure.severity_level.CRITICAL)
@allure.link('https://demoqa.com/automation-practice-form', name='Registration Form')
@allure.description("""
Проверка успешной регистрации пользователя с валидными данными на странице регистрации DemoQA.
Тест заполняет форму регистрации и проверяет соответствие введённых данных с отображаемыми после отправки формы.
""")
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

    with allure.step('Открытие страницы регистрации'):
        registration_page.open()

    with allure.step('Заполнение формы регистрации и отправка данных'):
        registration_page.register(user)

    with allure.step('Проверка успешной регистрации и отображения введённых данных'):
        registration_page.should_have_registered(expected_results)
