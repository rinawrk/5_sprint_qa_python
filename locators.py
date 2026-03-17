from selenium.webdriver.common.by import By


class RegisterPageLocators:
    # Поле ввода имени на странице регистрации
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/../input")

    # Поле ввода email на странице регистрации
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/../input")

    # Поле ввода пароля на странице регистрации
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/../input")

    # Кнопка "Зарегистрироваться" на странице регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

    # Ссылка "Войти" на странице регистрации
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")

    # Сообщение об ошибке при некорректном пароле
    INCORRECT_PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")


class LoginPageLocators:
    # Поле ввода email на странице входа
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/../input")

    # Поле ввода пароля на странице входа
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/../input")

    # Кнопка "Войти" на странице входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    # Ссылка "Зарегистрироваться" на странице входа
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")

    # Ссылка "Восстановить пароль" на странице входа
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")


class ForgotPasswordPageLocators:
    # Ссылка "Войти" на странице восстановления пароля
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


class ProfilePageLocators:
    # Кнопка "Выход" в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")


class MainPageLocators:
    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Кнопка "Личный Кабинет" в шапке сайта
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")

    # Кнопка "Конструктор" в шапке сайта
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")

    # Логотип Stellar Burgers в шапке сайта
    LOGO = (By.CSS_SELECTOR, "div[class*='AppHeader_header__logo'] a")

    # Кнопка "Оформить заказ" для авторизованного пользователя
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")


class ConstructorPageLocators:
    # Вкладка "Булки" в конструкторе
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/..")

    # Вкладка "Соусы" в конструкторе
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/..")

    # Вкладка "Начинки" в конструкторе
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/..")

    # Активная вкладка "Булки" в конструкторе
    ACTIVE_BUNS_TAB = (
        By.XPATH,
        "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Булки']"
    )

    # Активная вкладка "Соусы" в конструкторе
    ACTIVE_SAUCES_TAB = (
        By.XPATH,
        "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Соусы']"
    )

    # Активная вкладка "Начинки" в конструкторе
    ACTIVE_FILLINGS_TAB = (
        By.XPATH,
        "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Начинки']"
    )
    