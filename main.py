from package_1.module_1 import Cliente, product_purchase,delete_purchase, update_address
from package_1.module_2 import *


# Crear un cliente
customer_1 = Cliente("Juan", "Pérez", 30, "juan@example.com", "Av. San Martín 345")
print(customer_1)

# Actualizar el domicilio del cliente
new_address = input("Ingrese el nuevo domicilio: ")
update_address(customer_1, new_address)

# Realizar una compra
product_purchase1 = input("¿Qué deseas comprar? ")
product_purchase(customer_1, product_purchase1, "efectivo")

# Eliminar la compra
delete_purchase(customer_1, product_purchase1)


