import allure
import pytest
from pages.question_page import MainPageScooter
from conftest import driver
from conftest import sections_test_data

@pytest.mark.usefixtures("driver")
class TestQuestionsSections:

    @allure.title('Проверка в раздела "Вопросы о важном"')
    @allure.description('На главной странице в разделе "Вопросы о важном" по нажатию на вопрос отображается соответствующий ответ')
    @pytest.mark.parametrize("num,text", sections_test_data)
    def test_get_answer(self, driver, num, text):
        question_section = MainPageScooter(driver)
        question_section.main_page()
        question_section.scroll_to_questions_section()
        question_section.wait_for_scroll_to_questions_section()
        question_section.click_question_button(num)
        current_answer = question_section.get_current_answer_text()
        question_section.wait_for_to_get_current_answer()
        assert current_answer == text