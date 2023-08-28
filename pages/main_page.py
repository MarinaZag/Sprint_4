from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePageScooter
from data.urls import TestUrls
import allure


class MainPageScooter:

    @allure.step('Главная страница')
    def main_page(self):
        self.start_page(TestUrls.START_PAGE_LINK)

    @allure.step('Перейти к разделу "Вопросы о важном"')
    def scroll_to_questions_section(self):
        self.scroll_to_element(MainPageLocators.QUESTIONS_SECTION)

    @allure.step('Нажать на вопрос')
    def click_question_button(self, num):
        self.wait_visibility_element(MainPageLocators.QUESTIONS_SECTION)
        questions = self.find_elements_located(MainPageLocators.QUESTIONS)
        questions[num - 1].click()

    @allure.step('Получить текст ответа')
    def get_current_answer_text(self):
        self.wait_visibility_element(MainPageLocators.CURRENT_ANSWER)
        return self.find_element(MainPageLocators.CURRENT_ANSWER).text

    @allure.step('Перейти к кнопке "Заказать"')
    def scroll_button_order(self):
        self.scroll_to_element(MainPageLocators.BUTTON_ORDER)

    @allure.step('Нажать на кнопку "Заказать"')
    def click_button_order(self):
        self.scroll_button_order()
        self.wait_element_click(MainPageLocators.BUTTON_ORDER)
        self.click_element(MainPageLocators.BUTTON_ORDER)


    @allure.step('Нажать на кнопку "Заказать"')
    def click_button_order_header(self):
        self.click_element(BasePageLocators.BUTTON_ORDER_HEADER)

    @allure.step('Нажать на логотип "Самокат"')
    def click_logo_scooter(self):
        self.click_element(BasePageLocators.LOGO_SCOOTER)


    @allure.step('Нажать на логотип "Яндекс"')
    def click_logo_yandex(self):
        self.click_element(BasePageLocators.LOGO_YANDEX)
