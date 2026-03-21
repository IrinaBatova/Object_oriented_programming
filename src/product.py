class Product:
    # Атрибуты класса (общие для всех)
    name: str # Название
    description: str # Описание
    price: float # Цена
    quantity: float # Количество в наличии


prod_1 = Product()
prod_2 = Product()

prod_1.name = 'Хлеб'
prod_1.price = 55
prod_2.name = 'Молоко'
prod_2.price = 75

print(prod_1)
print(prod_2.name)