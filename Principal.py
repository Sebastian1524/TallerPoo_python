# +++ Codigo principal +++
from cliente import cliente
from saludo import saludo
# Creo el odjeto cliente

objcliente=cliente()
objsaludo=saludo()

# LLamo a los metodos del objeto

objcliente.tomar_datos()
aux_mensaje=objsaludo.hacer_saludo_formal()
objcliente.hacer_saludo(aux_mensaje)