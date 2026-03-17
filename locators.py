# Локаторы для страницы регистрации

NAME_INPUT = (By.XPATH, "//label[text()='Имя']/../input")
EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/../input")
PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
INCORRECT_PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")

# Локаторы для страницы входа

EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/../input")
PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

# Локаторы для страницы восстановления пароля

LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")