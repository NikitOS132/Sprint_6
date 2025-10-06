from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure
from locators.main_page_locators import MainPageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Подождать прогрузки элемента')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located(locator))
    
    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ввести значение в поле ввода')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Получить текст на элемента')
    def get_text_on_element(self, locator):
        return self.driver.find_element(*locator).text
    
    @allure.step('Перейти на другую вкладку')
    def switch_to_next_tab(self, timeout=10, index=1):
        WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > index)
        self.driver.switch_to.window(self.driver.window_handles[index])

    @allure.step('Получить заголовок страницы')
    def get_page_title(self):
        return self.driver.title
    
    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()