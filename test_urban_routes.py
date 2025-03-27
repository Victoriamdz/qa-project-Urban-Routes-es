import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data
import selectors 
from urban_routes_page import UrbanRoutesPage
from utils import retrieve_phone_code

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        """Configura el driver para Chrome."""
        options = webdriver.ChromeOptions()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)

    def test_set_route(self):
        """Verifica que las direcciones de origen y destino se establecen correctamente."""
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)

        assert self.driver.find_element(*selectors.from_field).get_property('value') == data.address_from
        assert self.driver.find_element(*selectors.to_field).get_property('value') == data.address_to

    def test_select_comfort_tariff(self):
        """Verifica que se selecciona la tarifa Comfort."""
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_comfort_tariff()

        assert self.driver.find_element(*selectors.comfort_tariff).is_displayed()

    def test_set_phone_number(self):
        """Prueba agregar número de teléfono."""
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_phone(data.phone_number)

        assert self.driver.find_element(*selectors.confirm_phone_button).is_displayed()

    def test_add_card(self):
        """Prueba agregar tarjeta de crédito."""
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_card_details(data.card_number, data.card_code)

        assert self.driver.find_element(*selectors.save_card_button).is_displayed()

    def test_write_message(self):
        """Verifica que se pueda enviar mensaje para el conductor."""
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_driver_message('Muéstrame el camino al museo')

        assert self.driver.find_element(*selectors.message_field).is_displayed()

    def test_select_blanket(self):
        """Prueba seleccionar una frazada."""
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_extras()

        assert self.driver.find_element(*selectors.blanket_checkbox).is_selected()

    def test_add_icecream(self):
        """Prueba añadir helados."""
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_extras()

        assert self.driver.find_element(*selectors.ice_cream_checkbox).is_selected()

    def test_find_driver(self):
        """Prueba la búsqueda de un conductor."""
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.place_order()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(selectors.driver_info))
        assert self.driver.find_element(*selectors.driver_info).is_displayed()

    @classmethod
    def teardown_class(cls):
        """Cierra el navegador al finalizar todas las pruebas."""
        cls.driver.quit()
