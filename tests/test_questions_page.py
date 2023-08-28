import allure
import pytest
from pages.main_page import MainPageScooter
from conftest import driver
from data.data import AnswerData

@pytest.mark.usefixtures("driver")
class TestQuestionsSections:

    @allure.title('Проверка в раздела "Вопросы о важном"')
    @allure.description('На главной странице в разделе "Вопросы о важном" по нажатию на вопрос отображается соответствующий ответ')
    @pytest.mark.parametrize("num,text", AnswerData.sections_test_data)
    def test_get_answer(self, driver, num, text):
        main_page = MainPageScooter(driver)
        main_page.main_url()
        main_page.scroll_to_questions_section()
        main_page.click_question_button(num)
        current_answer = main_page.get_current_answer_text()
        assert current_answer == text