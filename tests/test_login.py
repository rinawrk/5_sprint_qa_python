from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import (
    BASE_URL,
    LOGIN_URL,
    REGISTER_URL,
    FORGOT_PASSWORD_URL,
    EXISTING_USER_EMAIL,
    EXISTING_USER_PASSWORD,
)
from locators import (
    MainPageLocators,
    LoginPageLocators,
    RegisterPageLocators,
    ForgotPasswordPageLocators,
)


class TestLogin:

    # Проверка входа по кнопке "Войти в аккаунт" на главной странице

    def test_login_from_main_page(self, driver):
        
        # На главной странице нажимаем кнопку "Войти в аккаунт"
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        # Ждём загрузки страницы логина
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )

        # Вводим данные существующего пользователя
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)

        # Нажимаем кнопку "Войти"
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Ждём загрузки главной страницы авторизованного пользователя
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON)
        )

        # Проверяем, что произошёл вход в аккаунт
        assert driver.current_url == BASE_URL
