# ChromeControler_NiikiisApp
Este script utiliza Selenium y el navegador Chrome para registrar tiempo en la plataforma de Niikiis.

# Variables
remoto: Si es True, el tiempo registrado será como trabajo remoto. Si es False, será como trabajo en presencial.

debug_without_imputar: Si es True, el tiempo no será registrado en Niikiis.

fecha: Puede ser 'hoy' o una fecha en formato dd/mm/aaaa.

email: Tu correo electrónico de Niikiis.

pwd: Tu contraseña de Niikiis.

# Uso
Asegúrate de tener instalado Selenium y el driver de Chrome.
Rellena las variables email y pwd con tus credenciales de Niikiis.
Ejecuta el script.

# Notas
El script espera 10 segundos después de registrar el tiempo para asegurarse de que se ha guardado correctamente.
Si tienes problemas con el script, revisa los mensajes de error que aparezcan en la consola.
