cfrom selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selectors import

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        from_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(selectors.from_field)
        )
        from_element.send_keys(from_address)

    def set_to(self, to_address):
        to_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(selectors.to_field)
        )
        to_element.send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*to_field).get_property('value')

    def select_comfort_tariff(self):
        self.driver.find_element(*selectors.comfort_tariff).click()

    def enter_phone(self, phone):
        self.driver.find_element(*selectors.phone_field).send_keys(phone)
        self.driver.find_element(*selectors.confirm_phone_button).click()

    def enter_card_details(self, card_number, cvv):
        self.driver.find_element(*selectors.card_number_field).send_keys(card_number)
        cvv_field = self.driver.find_element(By.ID, 'code')
        cvv_field.send_keys(cvv)
        cvv_field.send_keys(Keys.TAB)
        self.driver.find_element(*selectors.save_card_button).click()

    def enter_driver_message(self, message):
        self.driver.find_element(*selectors.message_field).send_keys(message)

    def select_extras(self):
        self.driver.find_element(*selectors.blanket_checkbox).click()
        self.driver.find_element(*selectors.tissues_checkbox).click()
        ice_cream = self.driver.find_element(*selectors.ice_cream_checkbox)
        ice_cream.click()
        ice_cream.click()

    def place_order(self):
        self.driver.find_element(*selectors.order_button).click()

    def wait_for_driver_info(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(selectors.driver_info))
