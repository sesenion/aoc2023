from aoc07 import Hand


def test_hand_values():
    assert Hand("A2345").hand_value == 0
    assert Hand("11345").hand_value == 1
    assert Hand("11344").hand_value == 2
    assert Hand("14344").hand_value == 3
    assert Hand("34344").hand_value == 4
    assert Hand("34444").hand_value == 5
    assert Hand("44444").hand_value == 6


def test_comp():
    assert Hand("AAAAA") > Hand("KKKKK")
    assert Hand("22222") > Hand("AAAAK")
    assert Hand("44222") > Hand("AAKKQ")


def test_comp2():
    assert Hand("44222", j_is_joker=True) > Hand("AAKKQ", j_is_joker=True)
    assert Hand("AAAAJ", j_is_joker=True) > Hand("AAKKQ", j_is_joker=True)
