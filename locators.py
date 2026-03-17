# Локаторы для страницы регистрации

NAME_INPUT = (By.XPATH, "//label[text()='Имя']/../input")
EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/../input")
PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
INCORRECT_PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")


