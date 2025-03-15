class cliente:
    def __init__(self):
        self.nombre_cliente=""
        self.apellido_cliente=""
    
    def get_nombre(self):
        return self.nombre_cliente
    def get_apellido(self):
        return self.apellido_cliente
    def set_apellido(self,dato_apellido):
        self.apellido_cliente=dato_apellido
    
    def set_nombre(self,dato_nombre):
        self.nombre_cliente=dato_nombre
        

    def tomar_datos(self):
        self.nombre_cliente=input("Digite el nombre cliente: ")
        self.apellido_cliente=input("Digite su apellido Cliente: ")

    def procesar_datos(self):
        aux=self.nombre_cliente  + " " + self.apellido_cliente
    
    def mostrar_info_cliente(self):
        print(f"Nombre cliente: {self.nombre_cliente} - Apellido Cliente: {self.apellido_cliente}")
    
    def hacer_saludo(self,datosaludo):
        print(f"{datosaludo}: {self.nombre_cliente} {self.apellido_cliente}")
    
