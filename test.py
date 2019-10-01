import unittest
import Game


def test_ability():
    Gun = Game.Ability("Strength", 50)
    assert Gun.name == "Strength"
    assert Gun.max_damage == 50
    #assert Gun.__repr__ == "Ability: {}, max damage: {}".format(Gun.name, Gun.max_damage)

def test_weapon():
    Strength = Game.Ability("Strength", 50)
    assert Strength.name == "Strength"
    assert Strength.max_damage == 50
    #assert Strength.__repr__ == "Ability: {}, max damage: {}".format(Strength.name, Strength.max_damage)

def test_armor():
    Helmet = Game.Armor("Helmet", 65)
    assert Helmet.name == "Helmet"
    assert Helmet.max_block == 65

def test_create_hero():
    Jill = Game.Hero("Jill", 100, 0, 0)
    assert Jill.name == "Jill"
    assert Jill.current_health == 100
    assert Jill.deaths == 0
    assert Jill.kills == 0
    Strength = Game.Ability("Strength", 50)
    Jill.add_ability(Strength)
    assert Jill.abilities[0].name == "Strength"
