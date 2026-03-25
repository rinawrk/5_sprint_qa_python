from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import BASE_URL, LOGIN_URL, PROFILE_URL, EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators


class TestPersonalAccount:

    # Проверка перехода в личный кабинет по кнопке "Личный Кабинет"

    def test_go_to_personal_account(self, driver):

        # Открываем страницу входа
        driver.get(LOGIN_URL)

        # Вводим данные существующего пользователя
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)

        # Нажимаем кнопку "Войти"
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Ждём загрузки главной страницы авторизованного пользователя
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON)
        )

        # Нажимаем кнопку "Личный Кабинет"
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Ждём загрузки страницы профиля
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
        )

        # Проверяем, что открылась страница личного кабинета
        assert driver.current_url == PROFILE_URL

    # Проверка перехода из личного кабинета в конструктор по кнопке "Конструктор"

    def test_go_to_constructor_by_constructor_button(self, driver):
        
        # Открываем страницу входа
        driver.get(LOGIN_URL)

        # Вводим данные существующего пользователя
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)

        # Нажимаем кнопку "Войти"
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Ждём загрузки главной страницы авторизованного пользователя
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON)
        )

        # Переходим в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Ждём загрузки страницы профиля
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
        )

        # Нажимаем кнопку "Конструктор"
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

        # Ждём загрузки главной страницы
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON)
        )

        # Проверяем, что открылась главная страница
        assert driver.current_url == BASE_URL

    # Проверка перехода из личного кабинета в конструктор по логотипу Stellar Burgers

    def test_go_to_constructor_by_logo(self, driver):
        
        # Открываем страницу входа
        driver.get(LOGIN_URL)

        # Вводим данные существующего пользователя
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)

        # Нажимаем кнопку "Войти"
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Ждём загрузки главной страницы авторизованного пользователя
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON)
        )

        # Переходим в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Ждём загрузки страницы профиля
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
        )

        # Нажимаем на логотип Stellar Burgers
        driver.find_element(*MainPageLocators.LOGO).click()

        # Ждём загрузки главной страницы
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON)
        )

        # Проверяем, что открылась главная страница
        assert driver.current_url == BASE_URL

    # Проверка выхода из аккаунта по кнопке "Выход"

    def test_logout_from_personal_account(self, driver):

        # Открываем страницу входа
        driver.get(LOGIN_URL)

        # Вводим данные существующего пользователя
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)

        # Нажимаем кнопку "Войти"
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Ждём загрузки главной страницы авторизованного пользователя
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON)
        )

        # Переходим в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Ждём загрузки страницы профиля
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
        )

        # Нажимаем кнопку "Выход"
        driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()

        # Ждём загрузки страницы входа
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )

        # Проверяем, что открылась страница входа
        assert driver.current_url == LOGIN_URL
        