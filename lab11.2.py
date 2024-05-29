class Restaraurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Ресторан называется:", self.restaurant_name)
        print("Тип ресторана:", self.cuisine_type)

    def open_restaurant(self):
        print("Ресторан", self.restaurant_name, " открыт")


rest_names = ("рЕсТоРаН", "р100ран4ик", "PIZZA")
rest_types = ("просто ресторан.", "ресторан бытсрого питания", "пиццерия")
for data in zip(rest_names, rest_types):
    rest = Restaraurant(data[0], data[1])
    rest.describe_restaurant()
