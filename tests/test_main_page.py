import allure
import pytest
from pages.main_page import MainPageScooter
from pages.order_page import OrderPageScooter
from pages.base_page import BasePageScooter
from data.urls import TestUrls
from conftest import driver


@pytest.mark.usefixtures("driver")
class TestLogoScooter:
    @allure.title('Проверка перехода по логотипу "Самокат"')
    @allure.description('По клику на логотип "Самокат" осуществляется переход на главную страницу')
    def test_base_page_transition_logo_scooter(self, driver):
        main_page = OrderPageScooter(driver)
        main_page.main_url()
        main_page.click_logo_yandex()
        url_logo_scooter = driver.current_url
        assert url_logo_scooter == TestUrls.START_PAGE_LINK


@pytest.mark.usefixtures("driver")
class TestLogoYandex:
    @allure.title('Проверка перехода по логотипу "Яндекс"')
    @allure.description('По клику на логотип "Яндекс" осуществляется переход на главную страницу Яндекса')
    def test_base_page_transition_logo_yandex(self, driver):
        main_page = OrderPageScooter(driver)
        main_page.main_url()
        main_page.click_logo_yandex()
        assert driver.current_url == TestUrls.DZEN_PAGE_LINK