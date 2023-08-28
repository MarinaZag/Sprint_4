from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageScooter:

    def __init__(self, driver):
        self.driver = driver

    def start_page(self, page_url):
        self.driver.get(page_url)

    def find_element(self, element):
        return self.driver.find_element(*element)

    def add_value(self, element, value):
        self.find_element(element).send_keys(value)

    def set_name(self, element, name):
        self.driver.find_element(element).send_keys(name)

    def set_surname(self, element, surname):
        self.driver.find_element(element).send_keys(surname)

    def set_address(self, element, address):
        self.driver.find_element(element).send_keys(address)

    def set_subway_station(self, element,  station):
        self.driver.find_element(element).send_keys(station)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(element))
        self.click_scrollable_subway_station()

    def set_phone_number(self, element, number):
        self.driver.find_element(element).send_keys(number)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(element))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(element))

    def click_element(self, element):
         self.find_element(element).click()

    def wait_element_click(self, element):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(element))

    def wait_visibility_element(self, element):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element))

    def cross_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def find_text(self, element):
        return self.find_element(element).text

    def wait_url_to_be(self, page_url):
        WebDriverWait(self.driver, 20).until(EC.url_to_be(page_url))

    def find_elements_located(self, element):
        return WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located(element))


    def set_comment(self, element, comment):
        self.driver.find_element(element).send_keys(comment)


    def wait_for_new_tab_is_opened(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.number_of_windows_to_be(2))

    def wait_until_page_is_loaded(self):
        WebDriverWait(self.driver, 7).until(expected_conditions.url_to_be(*TestUrls.DZEN_PAGE_LINK))



