from project import Cat
from project import Vegetable, Fruit, Meat

cat = Cat("Harry", 10, "basement")

veg = Vegetable(7)

fruit = Fruit(5)

meat = Meat(9)

print(cat)

print(cat.make_sound())


print(cat.feed(fruit))
cat.feed(fruit)

cat.feed(meat)

print(cat)



