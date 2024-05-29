class Restaraurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print("Ресторан называется:", self.restaurant_name)
        print("Тип ресторана:", self.cuisine_type, ";  Рейтиг", self.rating)

    def open_restaurant(self):
        print("Ресторан", self.restaurant_name, " открыт")

    def update_rating(self, newrating):
        self.rating = newrating


class IceCreamStand(Restaraurant):
    def __init__(self, restaurant_name, cuisine_type, rating=0, flavors=[]):
        Restaraurant.__init__(self, restaurant_name, cuisine_type, rating=0)
        self.flavors = flavors

    def show_flavors(self):
        print("Доступные вкусы:")
        for item in self.flavors:
            print(item)


flavors_list = ['vanilla', 'strawberry', 'chocolate']
testrest = IceCreamStand("newRestaurant", "суши", 25, flavors_list)
testrest.show_flavors()
