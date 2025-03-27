from selenium.webdriver.common.by import By

# Campos de entrada
from_field = (By.ID, 'from')
to_field = (By.ID, 'to')

# Tarifa
comfort_tariff = (By.ID, 'tariff-comfort')

# Número de teléfono
phone_field = (By.ID, 'phone')
confirm_phone_button = (By.ID, 'confirm-phone')

# Método de pago
card_number_field = (By.ID, 'card-number')
save_card_button = (By.ID, 'save-card')

# Mensaje para el conductor
message_field = (By.ID, 'driver-message')

# Checkboxes de opciones extra
blanket_checkbox = (By.ID, 'option-blanket')
tissues_checkbox = (By.ID, 'option-tissues')
ice_cream_checkbox = (By.ID, 'option-ice-cream')

# Botón para ordenar
order_button = (By.ID, 'order-ride')

# Información del conductor
driver_info = (By.CLASS_NAME, 'driver-info')
