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


testrest=Restaraurant("newRestaurant","суши",25)
testrest.describe_restaurant()
testrest.update_rating(float(input("Оцените ресторан")))
testrest.describe_restaurant()