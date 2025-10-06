import allure
import pytest
from data import TestData
from pages.main_page import MainPage

class TestMainPageFaq:
    @allure.title('Проверка раздела "Вопросы о важном"')
    @pytest.mark.parametrize('question_number, expected_answer', TestData.test_data_question_answer)
    def test_click_faq_expand_icons_text_is_expected(self, driver, question_number, expected_answer):
        page = MainPage(driver)
        page.scroll_to_faq_section()
        page.wait_visibility_of_faq_item(question_number)
        page.click_on_faq_item(question_number)
        page.wait_visibility_of_faq_answer(question_number)
        actual = page.get_faq_answer_text(question_number)
        assert actual == expected_answer