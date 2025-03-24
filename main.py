from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import data


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    call_taxi_button = (By.ID, 'call-taxi')
    comfort_tariff = (By.CLASS_NAME, 'tariff-comfort')
    phone_field = (By.ID, 'phone')
    confirm_phone_button = (By.ID, 'confirm-phone')
    card_number_field = (By.ID, 'card-number')
    save_card_button = (By.ID, 'save-card')
    message_field = (By.ID, 'driver-message')
    blanket_checkbox = (By.ID, 'option-blanket')
    tissues_checkbox = (By.ID, 'option-tissues')
    ice_cream_checkbox = (By.ID, 'option-ice-cream')
    order_button = (By.ID, 'order-ride')
    driver_info = (By.CLASS_NAME, 'driver-info')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        from_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.from_field)
        )
        from_element.send_keys(from_address)

    def set_to(self, to_address):
        to_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.to_field)
        )
        to_element.send_keys(to_address)

    def call_taxi(self):
        self.driver.find_element(*self.call_taxi_button).click()

    def select_comfort_tariff(self):
        self.driver.find_element(*self.comfort_tariff).click()

    def enter_phone(self, phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)
        self.driver.find_element(*self.confirm_phone_button).click()

    def enter_card_details(self, card_number, cvv):
        self.driver.find_element(*self.card_number_field).send_keys(card_number)
        cvv_field = self.driver.find_element(By.ID, 'code')
        cvv_field.send_keys(cvv)
        cvv_field.send_keys(Keys.TAB)
        self.driver.find_element(*self.save_card_button).click()

    def enter_driver_message(self, message):
        self.driver.find_element(*self.message_field).send_keys(message)

    def select_extras(self):
        self.driver.find_element(*self.blanket_checkbox).click()
        self.driver.find_element(*self.tissues_checkbox).click()
        ice_cream = self.driver.find_element(*self.ice_cream_checkbox)
        ice_cream.click()
        ice_cream.click()

    def place_order(self):
        self.driver.find_element(*self.order_button).click()

    def wait_for_driver_info(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.driver_info))


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        options = webdriver.ChromeOptions()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        routes_page.call_taxi()
        assert routes_page.get_from() == data.address_from
        assert routes_page.get_to() == data.address_to

    def test_set_comfort(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_comfort_tariff()

    def test_set_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_phone(data.phone_number)

    def test_add_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_card_details(data.card_number, data.card_code)

    def test_write_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_driver_message('Muéstrame el camino al museo')

    def test_blanket(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_extras()

    def test_find_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.place_order()

    def test_wait_driver_information(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_driver_info()
        assert self.driver.find_element(*UrbanRoutesPage.driver_info).is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
