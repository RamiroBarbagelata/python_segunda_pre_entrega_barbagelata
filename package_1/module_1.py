class Cliente:
    def __init__(self, name, last_name, age, email, address):
        self.name = name 
        self.last_name = last_name
        self.age = age
        self.email = email
        self.address = address
        self.product = ""
    
    def __str__(self):
        return f"Fue un exito el registro de {self.name} {self.last_name} {self.age} años {self.email} que vive en {self.address}"
        
    def product_purchase(self, product, payment_method):
        print(f"{self.name} {self.last_name} compro {product} con {payment_method}")
            

def delete_purchase(customer, product):
    if customer.product == customer.product:
        print(f"{customer.name} {customer.last_name} elimino la compra de {product} de su carrito de compras.")
        customer.product = ""
    else:
        print("No hay ninguna compra para eliminar")