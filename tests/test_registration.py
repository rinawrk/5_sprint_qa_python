from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import LOGIN_URL, REGISTER_URL
from generators import (
    generate_name,
    generate_email,
    generate_valid_password,
    generate_invalid_password,
)
from locators import RegisterPageLocators, LoginPageLocators


class TestRegistration:

    # Проверка успешной регистрации нового пользователя

    def test_successful_registration(self, driver):
        
        # Открываем страницу регистрации
        driver.get(REGISTER_URL)

        # Генерируем данные нового пользователя
        name = generate_name()
        email = generate_email()
        password = generate_valid_password()

        # Заполняем форму регистрации
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)

        # Нажимаем кнопку "Зарегистрироваться"
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        # Ждём загрузки страницы логина
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )

        # Проверяем, что произошёл редирект на страницу логина
        assert driver.current_url == LOGIN_URL

    # Проверка появления ошибки при регистрации с коротким паролем

    def test_registration_with_short_password_shows_error(self, driver):
        # Открываем страницу регистрации
        driver.get(REGISTER_URL)

        # Генерируем данные пользователя
        name = generate_name()
        email = generate_email()
        password = generate_invalid_password()

        # Заполняем форму регистрации
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)

        # Нажимаем кнопку "Зарегистрироваться"
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        # Ждём появления сообщения об ошибке
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegisterPageLocators.INCORRECT_PASSWORD_ERROR)
        )

        # Проверяем, что остались на странице регистрации
        assert driver.current_url == REGISTER_URL

        # Проверяем текст ошибки
        error_text = driver.find_element(
            *RegisterPageLocators.INCORRECT_PASSWORD_ERROR
        ).text
        assert error_text == "Некорректный пароль"
