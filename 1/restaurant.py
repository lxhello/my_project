class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"this restaurant name is {self.restaurant_name}")
        print(f"this restaurant is {self.cuisine_type}")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['strawberry','grape','apple','blueberry']

    def show_flavors(self):
        print(f"this IceCreamStand has {self.flavors}")


my_restaurant = IceCreamStand('"home of food"','opening')
print(my_restaurant.describe_restaurant())
my_restaurant.show_flavors()