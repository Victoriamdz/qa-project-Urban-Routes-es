from selenium.webdriver.common.by import By

#  Campos de entrada
from_field = (By.ID, 'from')
to_field = (By.ID, 'to')

#  Botón "Pedir un taxi"
pedir_taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')


#  Tarifa Comfort
comfort_tariff = comfort_tariff = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")

#  Número de teléfono
phone_field = (By.XPATH, "//div[text()='Número de teléfono']/following-sibling::input")
confirm_phone_button = (By.XPATH, "//button[text()='Confirmar']")

# Método de pago
card_number_field = (By.XPATH, "//div[text()='Método de pago']/following-sibling::input")
save_card_button = (By.XPATH, "//button[text()='Agregar']")

# Mensaje para el conductor
message_field = (By.XPATH, "//label[text()='Mensaje para el conductor…']/following-sibling::textarea")

#  Checkboxes de opciones extra
blanket_checkbox = (By.XPATH, "//span[@class='slider round']")


ice_cream_checkbox = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')

#  Botón para ordenar viaje
order_button = (By.XPATH, "//span[text()='Introducir un número de teléfono y reservar']")

#  Información del conductor
driver_info = (By.XPATH, '//div[contains(@class, "driver-info")]')
