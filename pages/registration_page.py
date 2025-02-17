from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PracticeFormPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://demoqa.com/automation-practice-form"

    def open(self):
        self.browser.get(self.url)

    def fill_first_name(self, first_name):
        self.browser.find_element(By.ID, "firstName").send_keys(first_name)

    def fill_last_name(self, last_name):
        self.browser.find_element(By.ID, "lastName").send_keys(last_name)

    def fill_email(self, email):
        self.browser.find_element(By.ID, "userEmail").send_keys(email)

    def select_gender(self, gender):
        gender_xpath = f"//label[text()='{gender}']"
        self.browser.find_element(By.XPATH, gender_xpath).click()

    def fill_user_number(self, user_number):
        self.browser.find_element(By.ID, "userNumber").send_keys(user_number)

    def pick_date_of_birth(self, year, month, day):
        self.browser.find_element(By.ID, "dateOfBirthInput").click()
        self.browser.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys(year)
        self.browser.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys(month)
        self.browser.find_element(By.XPATH, f"//div[text()='{day}']").click()

    def fill_subject(self, subject):
        subject_input = self.browser.find_element(By.ID, "subjectsInput")
        subject_input.send_keys(subject)
        subject_input.send_keys("\n")  # Enter to select subject

    def remove_ads_iframe(self):
        """Удаляет рекламные iframe, чтобы избежать ошибок при клике."""
        self.browser.execute_script("""
            let iframes = document.querySelectorAll("iframe");
            iframes.forEach(iframe => iframe.remove());
        """)

    def choose_interest_reading(self):
        """Выбирает хобби 'Reading' и удаляет рекламные iframes перед этим."""
        self.remove_ads_iframe()  # Удаляем рекламу
        element = self.browser.find_element(By.XPATH, "//label[text()='Reading']")
        self.browser.execute_script("arguments[0].scrollIntoView();", element)  # Скроллим к элементу
        self.browser.execute_script("arguments[0].click();", element)  # Кликаем через JS

    def upload_picture(self, file_name):
        """Загружает картинку."""
        from data.resources import path  # Импорт функции для получения пути к файлу
        file_path = path(file_name)
        self.browser.find_element(By.ID, "uploadPicture").send_keys(file_path)

    def fill_address(self, address):
        self.browser.find_element(By.ID, "currentAddress").send_keys(address)

    def choose_state(self, state):
        self.browser.find_element(By.ID, "state").click()
        self.browser.find_element(By.XPATH, f"//div[text()='{state}']").click()

    def choose_city(self, city):
        self.browser.find_element(By.ID, "city").click()
        self.browser.find_element(By.XPATH, f"//div[text()='{city}']").click()

    def submit_button(self):
        self.browser.find_element(By.ID, "submit").click()

    def should_registered_user_with(self, *expected_values):
        """Проверяет, что отправленные данные совпадают с переданными значениями."""
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "modal-content"))
        )
        rows = self.browser.find_elements(By.XPATH, "//tbody/tr/td[2]")
        actual_values = [row.text for row in rows]

        assert actual_values == list(expected_values), f"Ожидалось {expected_values}, но получили {actual_values}"
