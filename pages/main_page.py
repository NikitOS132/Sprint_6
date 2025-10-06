import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    @allure.step('Подождать прогрузки кнопки "Заказать" в хедере')
    def wait_visibility_of_order_button_in_header(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(MainPageLocators.order_button_in_header))

    @allure.step('Кликнуть по кнопке "Заказать" в хедере')
    def click_on_order_button_in_header(self):
        self.click_on_element(MainPageLocators.order_button_in_header)

    @allure.step('Подождать прогрузки части лого с надписью "Самокат" в хедере')
    def wait_visibility_of_header_logo_scooter(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(MainPageLocators.header_logo_scooter))
    
    @allure.step('Подождать прогрузки части лого с надписью "Яндекс" в хедере')
    def wait_visibility_of_header_logo_yandex(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(MainPageLocators.header_logo_yandex))

    @allure.step('Кликнуть по части лого с надписью "Самокат" в хедере')
    def click_on_header_logo_scooter(self):
       self.click_on_element(MainPageLocators.header_logo_scooter)

    @allure.step('Кликнуть по части лого с надписью "Яндекс" в хедере')
    def click_on_header_logo_yandex(self):
        self.click_on_element(MainPageLocators.header_logo_yandex)

    @allure.step('Подождать прогрузки отображения заголовка главной страницы')
    def wait_visibility_of_main_header(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(MainPageLocators.main_header))
    
    @allure.step('Проверить отображение заголовка главной страницы')
    def check_displaying_of_main_header(self):
        return self.check_displaying_of_element(MainPageLocators.main_header)

    @allure.step('Проскроллить до секции "Вопросы о важном"')
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.faq_section)

    @allure.step('Ждём видимость вопроса с номером {index}')
    def wait_visibility_of_faq_item(self, index, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(MainPageLocators.faq_questions_items[index]))

    @allure.step('Кликаем по вопросу с номером {index}')
    def click_on_faq_item(self, index, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(MainPageLocators.faq_questions_items[index])).click()

    @allure.step('Ждём видимость ответа для вопроса {index}')
    def wait_visibility_of_faq_answer(self, index, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(MainPageLocators.faq_answers_items[index]))

    @allure.step('Берём текст ответа для вопроса {index}')
    def get_faq_answer_text(self, index):
        return self.get_text_on_element(MainPageLocators.faq_answers_items[index])