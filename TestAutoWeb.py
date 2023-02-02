from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime

#Vars
remoto = True
debug_without_imputar = False
fecha = 'hoy' # elegir entre 'hoy' o '01/02/2023' format
email = "YOUR_EMAIL"
pwd = "YOUR_PASSWORD"

# Inicializa el driver de Chrome
driver = webdriver.Chrome()

# Abre la página de inicio de sesión de niikiis
driver.get("https://app.niikiis.com/calendar/attendance")

# abre nueva tab con intro de john cena para sentirte bien mientras cumples con tu empresa
# driver.execute_script("window.open('https://www.youtube.com/watch?v=2D-ZO2rGcSA','_blank');")
# sleep(2)

# acceptarcookies = driver.find_elements(By.CSS_SELECTOR, 'button.yt-spec-button-shape-next--filled')[3]
# acceptarcookies.click()

# driver.switch_to.window(driver.window_handles[0])

# Encuentra el elemento de entrada de usuario y contraseña y envía las credenciales
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'user_email'))
)
username = driver.find_element(By.NAME, 'user_email')
password = driver.find_element(By.NAME,'user_password')
sleep(1)
username.send_keys(email)
password.send_keys(pwd)

password.send_keys(Keys.RETURN)


element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'button.sc-dRCTWM'))
)

# Espera a que cargue la página 
sleep(2)

# pagina de meter horas
driver.get("https://app.niikiis.com/calendar/attendance")

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'button.sc-GMQeP'))
)

# Click en Crear Sesiones
crearSesiones = driver.find_elements(By.CSS_SELECTOR, 'button.sc-GMQeP')[1]
crearSesiones.send_keys(Keys.RETURN)
sleep(1)

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'button.sc-GMQeP'))
)

if(remoto == True):
    # Click en remoto
    remotoBtn = driver.find_element(By.CSS_SELECTOR, 'p.hfQvwW')
    remotoBtn.click() # .send_keys(Keys.ENTER)
else:
    # Click en presencial
    remotoBtn = driver.find_element(By.CSS_SELECTOR, 'p.bfPiTT')
    remotoBtn.click()  #.send_keys(Keys.RETURN)


checkin = driver.find_elements(By.CSS_SELECTOR, 'input.sc-RbTVP')[0]
checkout = driver.find_elements(By.CSS_SELECTOR, 'input.sc-RbTVP')[1]

# fecha a imputar
if(fecha == 'hoy'):
    fecha = datetime.now().date().strftime("%d/%m/%Y")

checkin.send_keys(fecha)
checkout.send_keys(fecha)

sleep(1)

#logear time
if(not(debug_without_imputar)):
    palante = driver.find_elements(By.CSS_SELECTOR, 'button.sc-GMQeP')[1]
    palante.send_keys(Keys.RETURN)

sleep(10)

# Cierra el driver
driver.close()