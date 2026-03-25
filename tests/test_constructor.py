from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import ConstructorPageLocators


class TestConstructor:

    # Проверка перехода к разделу "Булки"
    
    def test_open_buns_tab(self, driver):

        # Сначала переходим в раздел "Соусы"
        driver.find_element(*ConstructorPageLocators.SAUCES_TAB).click()

        # Ждём, пока вкладка "Соусы" станет активной
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_SAUCES_TAB)
        )

        # Переходим в раздел "Булки"
        driver.find_element(*ConstructorPageLocators.BUNS_TAB).click()

        # Ждём, пока вкладка "Булки" станет активной
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_BUNS_TAB)
        )

        # Проверяем, что вкладка "Булки" активна
        assert driver.find_element(*ConstructorPageLocators.ACTIVE_BUNS_TAB).is_displayed()

    # Проверка перехода к разделу "Соусы"

    def test_open_sauces_tab(self, driver):

        # Переходим в раздел "Соусы"
        driver.find_element(*ConstructorPageLocators.SAUCES_TAB).click()

        # Ждём, пока вкладка "Соусы" станет активной
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_SAUCES_TAB)
        )

        # Проверяем, что вкладка "Соусы" активна
        assert driver.find_element(*ConstructorPageLocators.ACTIVE_SAUCES_TAB).is_displayed()
