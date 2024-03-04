from package_1.module_1 import Cliente, delete_purchase
from package_1.module_2 import update_address


# Crear un cliente
customer_1 = Cliente("Juan", "Pérez", 30, "juan@example.com", "Av. San Martín 345")
print(customer_1)

# Actualizar el domicilio del cliente
new_address = input("Ingrese el nuevo domicilio: ")
update_address(customer_1, "Calle Falsa 4321")

# Realizar una compra
customer_1.product_purchase("PlayStation 5", "tarjeta de crédito")

# Eliminar la compra
delete_purchase(customer_1, "PlayStation 5")


