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
       
        options = webdriver.ChromeOptions()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get(data.urban_routes_url)

    def test_set_route(self):
        
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)

        assert routes_page.get_from() == data.address_from
        assert routes_page.get_to() == data.address_to

    def test_select_comfort_tariff(self):
        
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_comfort_tariff()

        assert routes_page.driver.find_element(*selectors.comfort_tariff).is_displayed()

    def test_set_phone_number(self):
       
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_phone(data.phone_number)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(selectors.confirm_phone_button)
        )
        assert self.driver.find_element(*selectors.confirm_phone_button).is_displayed()

        
        phone_code = retrieve_phone_code(self.driver)
        assert phone_code is not None and phone_code.isdigit()

    def test_add_card(self):
    
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_card_details(data.card_number, data.card_code)

        assert routes_page.driver.find_element(*selectors.save_card_button).is_displayed()

    def test_write_message(self):
       
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_driver_message('Muéstrame el camino al museo')

        assert routes_page.driver.find_element(*selectors.message_field).is_displayed()

    def test_select_extras(self):
        
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_extras()

        assert routes_page.driver.find_element(*selectors.blanket_checkbox).is_selected()
        assert routes_page.driver.find_element(*selectors.ice_cream_checkbox).is_selected()

    def test_find_driver(self):
       
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.place_order()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(selectors.driver_info)
        )
        assert routes_page.driver.find_element(*selectors.driver_info).is_displayed()

    @classmethod
    def teardown_class(cls):
        
        cls.driver.quit()
