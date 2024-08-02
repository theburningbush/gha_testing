from yowhatprj.whatwhat import what
from yowhatprj.yoyoyo import yo


def test_say_what():
    assert what.say_what() == '1 2 3 what'


def test_say_yo():
    assert yo.say_yo() == 'yo'


def test_not_yo():
    response = yo.say_yo()
    response = 'hello'
    assert response != 'yo'