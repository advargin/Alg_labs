class Restaraurant:
    def __init__(self,restaurant_name, cuisine_type,rating=0):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.rating=rating

    def describe_restaurant(self):
        print ("Ресторан называется:",self.restaurant_name)
        print("Тип ресторана:", self.cuisine_type, ";  Рейтиг" , self.rating)
    def open_restaurant(self):
        print ("Ресторан", self.restaurant_name, " открыт")
    def update_rating(self,newrating):
        self.rating=newrating

class IceCreamStand(Restaraurant):
    def __init__(self, restaurant_name, cuisine_type,location='',opening_hours='',rating=0,flavors=[]):
        Restaraurant.__init__(self,restaurant_name, cuisine_type,rating=0)
        self.flavors=flavors
        self.location=location
        self.opening_hours=opening_hours
    def show_flavors(self):
        print()
        print("Доступные вкусы:")
        for item in self.flavors:
            print(item)
    def add_flavor(self,someflavor):
        if someflavor not in self.flavors:
            self.flavors.append(someflavor)
        else:
            print ('Такой вкус уже есть')
    def delete_flavor(self,someflavor):
        if someflavor in self.flavors:
            self.flavors.remove(someflavor)
            print ("Вкус удален")
    def check_flavor(self,someflavor):
        if someflavor in self.flavors:
            print('Такой вкус есть в наличии')
            return True
        else:
            print('Такого вкуса нет в наличии')
            return False



flavors_list=['vanilla','strawberry','chocolate']
testrest=IceCreamStand("newRestaurant","суши",flavors=flavors_list,location='somewhere')
#изначальый список вкусов
testrest.show_flavors()
testrest.delete_flavor("vanilla")
testrest.add_flavor("lemon")
#добавили и удалили какие то вкусы
testrest.show_flavors()
testrest.describe_restaurant()
#проверяем, есть ли вкус в наличии..
testrest.check_flavor("арбуз")
testrest.check_flavor("chocolate")