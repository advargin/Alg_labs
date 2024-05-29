class Restaraurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print ("Ресторан называется:",self.restaurant_name)
        print("Тип ресторана:", self.cuisine_type)
    def open_restaurant(self):
        print ("Ресторан", self.restaurant_name, " открыт")
testrest=Restaraurant("newRestaurant","суши")
print(testrest.restaurant_name,testrest.cuisine_type)
testrest.describe_restaurant()
testrest.open_restaurant()