import unittest

from project.hero import Hero


class HeroTest(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Hero", 1, 100, 100)
        self.enemy = Hero("Enemy", 1, 50, 50)

    def test_init(self):
        self.assertEqual(self.hero.username, "Hero")
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 100)

    def test_battle_with_yourself__raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_battle_with_not_enough_health__raise_value_erorr(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(Hero("Elton", 10, 10, 10))

        self.assertEqual(str(ve.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_with_enemy_with_not_enough_health__raise_value_erorr(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(str(ve.exception), "You cannot fight Enemy. He needs to rest")

    def test_battle_draw(self):
        self.hero.health = self.enemy.health
        self.hero.damage = self.enemy.damage
        battle_result = self.hero.battle(self.enemy)

        self.assertEqual(battle_result, "Draw")

    def test_battle_win(self):
        battle_result = self.hero.battle(self.enemy)

        self.assertEqual(battle_result, "You win")
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 55)
        self.assertEqual(self.hero.damage, 105)

    def test_battle_lose(self):
        self.hero.health = 25
        self.hero.damage = 25
        battle_result = self.hero.battle(self.enemy)

        self.assertEqual(battle_result, "You lose")
        self.assertEqual(self.enemy.level, 2)
        self.assertEqual(self.enemy.health, 30)
        self.assertEqual(self.enemy.damage, 55)

    def test__str__method(self):
        expected_result = f"Hero Hero: 1 lvl\nHealth: 100\nDamage: 100\n"
        actual_result = str(self.hero)

        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()