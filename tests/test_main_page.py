import allure
import pytest
from pages.main_page import BasePageScooter
from pages.order_page import OrderPageScooter
from conftest import driver, START_PAGE_LINK, DZEN_PAGE_LINK

@pytest.mark.usefixtures("driver")
class TestLogoScooter:
    @allure.title('Проверка перехода по логотипу "Самокат"')
    @allure.description('По клику на логотип "Самокат" осуществляется переход на главную страницу')
    def test_base_page_transition_logo_scooter(self, driver):
        open_order_page = OrderPageScooter(driver)
        open_order_page.order_page()
        transition_logo_scooter = BasePageScooter(driver)
        transition_logo_scooter.click_logo_scooter()
        transition_logo_scooter.wait_for_logo_scooter()
        url_logo_scooter = driver.current_url
        assert url_logo_scooter == START_PAGE_LINK


@pytest.mark.usefixtures("driver")
class TestLogoYandex:
    @allure.title('Проверка перехода по логотипу "Яндекс"')
    @allure.description('По клику на логотип "Яндекс" осуществляется переход на главную страницу Яндекса')
    def test_base_page_transition_logo_yandex(self, driver):
        open_order_page = OrderPageScooter(driver)
        open_order_page.order_page()
        transition_logo_yandex = BasePageScooter(driver)
        transition_logo_yandex.click_logo_yandex()
        transition_logo_yandex.wait_for_new_tab_is_opened()
        driver.switch_to.window(driver.window_handles[1])
        transition_logo_yandex.wait_until_page_is_loaded()
        assert driver.current_url == DZEN_PAGE_LINK