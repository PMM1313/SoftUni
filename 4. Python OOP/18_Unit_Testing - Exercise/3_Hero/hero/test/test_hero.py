from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    username = "Test hero"
    level = 5
    health = 12.3
    damage = 9.8

    def setUp(self):
        self.hero = Hero(self.username, self.level, self. health, self.damage)

    def test_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_attr_types(self):
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.level, int)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.damage, float)

    def test_hero_enemy_same_names(self):
        enemy = Hero(self.username, self.level, self. health, self.damage)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_not_enough_health(self):
        self.hero.health = 0
        enemy = Hero("Enemy", self.level, self.health, self.damage)

        with self.assertRaises(ValueError) as e:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(e.exception))

        self.hero.health = -1
        with self.assertRaises(ValueError) as e:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(e.exception))

    def test_enemy_not_enough_health(self):
        enemy = Hero("Enemy", self.level, 0, self.damage)
        with self.assertRaises(ValueError) as e:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(e.exception))

        enemy.health = -1
        with self.assertRaises(ValueError) as e:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(e.exception))

    def test_draw(self):
        enemy = Hero("Enemy", self.level, self.health, self.damage)

        result = self.hero.battle(enemy)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(-36.7, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

        self.assertEqual(self.level, enemy.level)
        self.assertEqual(-36.7, enemy.health)
        self.assertEqual(self.damage, enemy.damage)

        self.assertEqual("Draw", result)

    def test_hero_wins(self):
        enemy = Hero("Enemy", 1, 1, 1)
        result = self.hero.battle(enemy)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(16.3, self.hero.health)
        self.assertEqual(14.8, self.hero.damage)
        self.assertEqual("You win", result)

        self.assertEqual(1, enemy.level)
        self.assertEqual(-48.0, enemy.health)
        self.assertEqual(1, enemy.damage)

    def test_hero_loses(self):
        enemy = Hero("Enemy", 100, 100, 100)
        result = self.hero.battle(enemy)

        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(-9987.7, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)
        self.assertEqual("You lose", result)

        self.assertEqual(101, enemy.level)
        self.assertEqual(56, enemy.health)
        self.assertEqual(105, enemy.damage)

    def test_str(self):
        expected = f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"

        self.assertEqual(expected, str(self.hero))









if __name__ == '__main':
    main()