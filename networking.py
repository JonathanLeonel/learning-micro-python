# traigo network
import network

#extraigo los modos station y ap interfaces de network
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)

# verifico si el modo está station activo
sta_if.active()

# verifico si el modo está ap activo
ap_if.active()

# activo el modo station
sta_if.active(True)

# conecto el módulo a mi red
sta_if.connect('<Nombre de red>', '<contraseña>')

# verifico si está conectado
sta_if.isconnected()

# verifico los datos de ip de la conexión (IP Address, Subnet Mask, Gateway IP Address, DNS Server)
sta_if.ifconfig()

