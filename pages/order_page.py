from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePageScooter
from data.urls import TestUrls
import allure


class OrderPageScooter:

    @allure.step('Открыть страницу заказа')
    def order_page(self):
        self.start_page(TestUrls.ORDER_PAGE_LINK)

    @allure.step('Выбрать станцию метро')  # done
    def choose_metro_station(self):
        self.click_element(OrderPageLocators.SCROLLABLE_FIELD_SUBWAY_STATION)
        self.click_element(OrderPageLocators.METRO_STATION_CLICK)

    @allure.step('Нажать на кнопку Далее')  # done
    def click_next_button(self):
        self.find_element(OrderPageLocators.BUTTON_FORWARD)
        self.click_element(OrderPageLocators.BUTTON_FORWARD)

    @allure.step('Заполнить поля в форме "Для кого самокат?"')  # DONE
    def filling_form_one(self, name=BasePageScooter.set_name(), surname=BasePageScooter.set_surname(),
                         address=BasePageScooter.set_address(),
                         number=BasePageScooter.set_phone_number()):  # заполнение формы Для кого самокат
        self.add_value(OrderPageLocators.FIELD_NAME, name)
        self.add_value(OrderPageLocators.FIELD_SURNAME, surname)
        self.add_value(OrderPageLocators.FIELD_ADDRESS, address)
        self.choose_metro_station()
        self.add_value(OrderPageLocators.FIELD_PHONE, number)
        self.click_button_forward()

    @allure.step('Выбрать дату "Когда привезти самокат?"')
    def set_date(self, date):
        self.find_element(OrderPageLocators.FIELD_CALENDAR).send_keys(date)
        self.wait_visibility_element(OrderPageLocators.CALENDAR) # Ждем пока появится календарь
        self.click_element(OrderPageLocators.DATE_PICKER_DAY_SELECTED)

    @ allure.step('Выбрать срок аренды')
    def select_rental_period(self):
        self.click_element(OrderPageLocators.FIELD_RENTAL_PERIOD)
        self.click_element(OrderPageLocators.CHOICE_RENT_PERIOD)

    @allure.step('Выбрать черный самокат')
    def click_checkbox_black(self):
        self.click_element(*OrderPageLocators.CHECKBOX_BLACK)

    @allure.step('Выбрать серый самокат')
    def click_checkbox_grey(self):
        self.click_element(*OrderPageLocators.CHECKBOX_GREY)

    @allure.step('Кликнуть на кнопку "Заказать"')
    def click_button_order(self):
        self.click_element(OrderPageLocators.BUTTON_ORDER)

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.click_element(OrderPageLocators.BUTTON_CONFIRMATION_ORDER)

    @allure.step('Заполнить поля в форме "Про аренду"')
    def filling_form_about_rent_one_flow(self, date, comment):  # заполнение формы Про аренду 1
        self.set_date(date)
        self.select_rental_period(OrderPageLocators.RENTAL_PERIOD_DAY)
        self.click_checkbox_grey()
        self.set_comment(comment)
        self.click_button_order()

    @allure.step('Заполнить поля в форме "Про аренду"')
    def filling_form_about_rent_two_flow(self, date, comment):  # заполнение формы Про аренду 2
        self.set_date(date)
        self.select_rental_period(OrderPageLocators.RENTAL_PERIOD_SEVEN_DAYS)
        self.click_checkbox_black()
        self.set_comment(comment)
        self.click_button_order()

    @allure.step('Посмотреть статус заказа')
    def click_button_view_status(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_VIEW_STATUS).click()
