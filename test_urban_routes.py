from selectors import driver_info, comfort_tariff, from_field, to_field, phone_field, confirm_phone_button, card_number_field, save_card_button, message_field, blanket_checkbox, tissues_checkbox, ice_cream_checkbox, order_button
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data
from urban_routes_page import UrbanRoutesPage
from utils import retrieve_phone_code

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        options = webdriver.ChromeOptions()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)

    def test_set_route(self):
        """Verifica que las direcciones de origen y destino se establecen correctamente."""
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)

        assert routes_page.get_from() == data.address_from
        assert routes_page.get_to() == data.address_to

    def test_select_comfort_tariff(self):
        """Verifica que se selecciona la tarifa Comfort."""
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_comfort_tariff()
        assert self.driver.find_element(*comfort_tariff).is_displayed()

    def test_set_phone_number(self):
        """Prueba agregar número de teléfono."""
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_phone(data.phone_number)
        assert self.driver.find_element(*confirm_phone_button).is_displayed()

    def test_add_card(self):
        """Prueba agregar tarjeta de crédito."""
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_card_details(data.card_number, data.card_code)
        assert self.driver.find_element(*save_card_button).is_displayed()

    def test_write_message(self):
        """Verifica que se pueda enviar mensaje para el conductor."""
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_driver_message('Muéstrame el camino al museo')
        assert self.driver.find_element(*message_field).is_displayed()

    def test_select_blanket(self):
        """Prueba seleccionar una frazada."""
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_extras()
        assert self.driver.find_element(*blanket_checkbox).is_selected()

    def test_add_icecream(self):
        """Prueba añadir helados."""
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_extras()
        assert self.driver.find_element(*ice_cream_checkbox).is_selected()

    def test_find_driver(self):
        """Prueba la búsqueda de un conductor."""
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.place_order()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(driver_info))
        assert self.driver.find_element(*driver_info).is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
