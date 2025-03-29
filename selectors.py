from selenium.webdriver.common.by import By

#  Campos de entrada
from_field = (By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[1]/div[2]/div[1]/label')
to_field = (By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[2]/div[2]/div[1]/label')

#  Botón "Pedir un taxi"
pedir_taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')


#  Tarifa Comfort
comfort_tariff = (By.XPATH, ‘//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/img')


#  Número de teléfono
phone_field = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div')
confirm_phone_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')

# Método de pago
card_number_field = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[1]')
save_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')

# Mensaje para el conductor
message_field = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[3]/div/label')

#  Checkboxes de opciones extra
blanket_checkbox = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')

ice_cream_checkbox = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')

#  Botón para ordenar viaje
order_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button')

#  Información del conductor
driver_info = (By.XPATH, '//div[contains(@class, "driver-info")]')
