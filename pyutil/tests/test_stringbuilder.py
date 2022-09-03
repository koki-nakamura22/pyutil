import pytest

from pyutil.string import StringBuilder


##############
# Constructor
##############
# Omit this test case because overlaps with len and to_str testings.
# def test_constructor_without_param():
#     pass

# Omit this test case because overlaps with len and to_str testings.
# def test_constructor_with_param():
#     pass

##############
# len
##############
def test_empty_string_len():
    sb = StringBuilder()
    assert sb.len() == 0


def test_string_len():
    sb = StringBuilder('HelloWorld')
    assert sb.len() == 10


##############
# to_str
##############
def test_empty_string_to_str():
    sb = StringBuilder()
    assert sb.to_str() == ''


def test_string_to_str():
    sb = StringBuilder('HelloWorld')
    assert sb.to_str() == 'HelloWorld'

##############
# append
##############


def test_append():
    sb = StringBuilder()
    sb.append('hoge')
    assert sb.to_str() == 'hoge'
    sb.append('fuga')
    assert sb.to_str() == 'hogefuga'


##############
# append_line
##############
def test_append_line():
    sb = StringBuilder()
    sb.append_line('hoge')
    assert sb.to_str() == """hoge
"""
    sb.append_line('fuga')
    assert sb.to_str() == """hoge
fuga
"""

##############
# insert
##############


def test_insert():
    sb = StringBuilder('hogefuga')
    sb.insert(4, 'piyo')
    assert sb.to_str() == 'hogepiyofuga'


def test_insert_with_invalid_pos():
    with pytest.raises(ValueError) as e:
        sb = StringBuilder('hogefuga')
        sb.insert(-1, 'piyo')

    assert str(e.value) == 'Invalid pos: -1'

##############
# remove
##############


def test_remove():
    sb = StringBuilder('hogefugapiyo')
    sb.remove(4, 4)
    assert sb.to_str() == 'hogepiyo'


def test_remove_with_invalid_start_index():
    with pytest.raises(ValueError) as e:
        sb = StringBuilder('hogefugapiyo')
        sb.remove(-1, 10)
    assert str(e.value) == 'Invalid start_index: -1'


def test_remove_with_invalid_len():
    with pytest.raises(ValueError) as e:
        sb = StringBuilder('hogefugapiyo')
        sb.remove(0, 0)
    assert str(e.value) == 'Invalid len: 0'


##############
# replace
##############
def test_replace():
    sb = StringBuilder()
    sb.append_line(
        'I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."')
    sb.append_line(
        'I have a dream that one day on the red hills of Georgia, the sons of former slaves and the sons of former slave owners will be able to sit down together at the table of brotherhood.')
    sb.replace('dream', 'big dream')
    assert sb.to_str(
    ) == """I have a big dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."
I have a big dream that one day on the red hills of Georgia, the sons of former slaves and the sons of former slave owners will be able to sit down together at the table of brotherhood.
"""

##############
# clear
##############


def test_clear():
    sb = StringBuilder('hogefuga')
    assert sb.len() == 8
    assert sb.to_str() == 'hogefuga'
    sb.clear()
    assert sb.len() == 0
    assert sb.to_str() == ''
