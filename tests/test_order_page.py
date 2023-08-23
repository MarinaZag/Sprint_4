import allure
import pytest
from pages.main_page import BasePageScooter
from pages.question_page import MainPageScooter
from pages.order_page import OrderPageScooter
from utils import get_random_phone_number, get_current_date, get_next_date
from conftest import driver



@pytest.mark.usefixtures("driver")
class TestOrderButtonMainPage:
    @allure.title('Проверка оформления заказа через кнопку "Заказать" на главной странице: с текущей датой')
    @allure.description('По клику на кнопку "Заказать", заполнить всю форму и проверить, что "Заказ оформлен"')
    def test_order_button_main_page_current_date_user_flow_positive(self, driver):
        click_button_order = MainPageScooter(driver)
        click_button_order.main_page()
        click_button_order.scroll_button_order()
        click_button_order.click_button_order()
        new_order = OrderPageScooter(driver)
        new_order.filling_form_one(
            name='Иван',
            surname='Иванов',
            address='Профсоюзная, 19',
            station='Профсоюзная',
            number=get_random_phone_number())
        new_order.wait_for_form_two()
        new_order.filling_form_about_rent_one_flow(
            date=get_current_date(),
            comment='Supper')
        new_order.wait_for_form_three()
        new_order.click_confirmation_order()
        new_order_title = new_order.get_new_order_title()
        new_order.wait_for_window_order_is_placed()
        assert new_order_title == 'Заказ оформлен'

    @allure.title(
        'Проверка оформления заказа через кнопку "Заказать" на главной странице: со следующей датой')
    @allure.description(
        'На странице найти и нажать кнопку "Заказать", заполнить весь флоу позитивного сценария и проверить, что "Заказ оформлен"')
    def test_order_button_main_page_next_date_user_flow_positive(self, driver):
        click_button_order = MainPageScooter(driver)
        click_button_order.main_page()
        click_button_order.scroll_button_order()
        click_button_order.click_button_order()
        new_order = OrderPageScooter(driver)
        new_order.filling_form_one(
            name='Иван',
            surname='Иванов',
            address='Профсоюзная, 19',
            station='Профсоюзная',
            number=get_random_phone_number())
        new_order.wait_for_form_two()
        new_order.filling_form_about_rent_two_flow(
            date=get_next_date(),
            comment='')
        new_order.wait_for_form_three()
        new_order.click_confirmation_order()
        new_order_title = new_order.get_new_order_title()
        new_order.wait_for_window_order_is_placed()
        assert new_order_title == 'Заказ оформлен'


@pytest.mark.usefixtures("driver")
class TestOrderButtonBasePage:
    @allure.title(
        'Проверка оформления заказа через кнопку "Заказать" в header: со текущей датой')
    @allure.description(
        'В header найти и нажать кнопку "Заказать", заполнить весь флоу позитивного сценария и проверить, что "Заказ оформлен"')
    def test_order_button_base_page_current_date_user_flow_positive(self, driver):
        open_main_page = MainPageScooter(driver)
        open_main_page.main_page()
        click_button_order = BasePageScooter(driver)
        click_button_order.click_button_order_header()
        new_order = OrderPageScooter(driver)
        new_order.filling_form_one(
            name='Иван',
            surname='Иванов',
            address='Профсоюзная, 19',
            station='Профсоюзная',
            number=get_random_phone_number())
        new_order.wait_for_form_two()
        new_order.filling_form_about_rent_one_flow(
            date=get_current_date(),
            comment='Supper')
        new_order.wait_for_form_three()
        new_order.click_confirmation_order()
        new_order_title = new_order.get_new_order_title()
        new_order.wait_for_window_order_is_placed()
        assert new_order_title == 'Заказ оформлен'

    @allure.title('Проверка оформления заказа через кнопку "Заказать" со следующей датой')
    @allure.description('По кликун на кнопку "Заказать", заполнить всю форму позитивного сценария и проверить, что "Заказ оформлен"')
    def test_order_button_base_page_next_date_user_flow_positive(self, driver):
        open_main_page = MainPageScooter(driver)
        open_main_page.main_page()
        click_button_order = BasePageScooter(driver)
        click_button_order.click_button_order_header()
        new_order = OrderPageScooter(driver)
        new_order.filling_form_one(
            name='Иван',
            surname='Иванов',
            address='Профсоюзная, 19',
            station='Профсоюзная',
            number=get_random_phone_number())
        new_order.wait_for_form_two()
        new_order.filling_form_about_rent_two_flow(
            date=get_next_date(),
            comment='')
        new_order.wait_for_form_three()
        new_order.click_confirmation_order()
        new_order_title = new_order.get_new_order_title()
        new_order.wait_for_window_order_is_placed()
        assert new_order_title == 'Заказ оформлен'