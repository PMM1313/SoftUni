from project.animals.birds import Owl, Hen
from project.food import Meat, Vegetable, Fruit, Seed

owl = Owl("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
seed = Seed(1)
print(owl)
print(owl.make_sound())
# owl.feed(veg)
# owl.feed(fruit)
# owl.feed(meat)
owl.feed(seed)
print(owl)

