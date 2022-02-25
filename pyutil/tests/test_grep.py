import os
import pytest
from pyutil.file import *

__FILE_DIR = os.path.dirname(__file__)
__TEST_FILE_DIR = os.path.join(__FILE_DIR, "for_test_grep")
__EMPTY_FILE_PATH = os.path.join(__TEST_FILE_DIR, "empty.txt")
__FOR_GREP_TEST_FILE_PATH = os.path.join(__TEST_FILE_DIR, "for_grep_test.txt")

#############
# grep test
#############


def test_grep_empty_file():
    assert grep(__EMPTY_FILE_PATH, "big") == []
    assert grep(__EMPTY_FILE_PATH, "big") == list()


def test_grep_keywords_none():
    with pytest.raises(TypeError):
        assert grep(__FOR_GREP_TEST_FILE_PATH, None)


def test_grep_one_keyword_exists():
    assert grep(__FOR_GREP_TEST_FILE_PATH, "big") == [
        {
            "no": 6,
            "text": "No big deal."
        }
    ]


def test_grep_multiple_keywords_exist():
    assert grep(__FOR_GREP_TEST_FILE_PATH, "She", "papers") == [
        {
            "no": 16,
            "text": "She refused to sign the final adoption papers."
        }
    ]


def test_grep_multiple_keywords_list_exist():
    assert grep(__FOR_GREP_TEST_FILE_PATH, *["She", "papers"]) == [
        {
            "no": 16,
            "text": "She refused to sign the final adoption papers."
        }
    ]


def test_grep_one_keyword_does_not_exists():
    assert grep(__FOR_GREP_TEST_FILE_PATH, "hogehoge") == []
    assert grep(__FOR_GREP_TEST_FILE_PATH, "hogehoge") == list()


def test_grep_multiple_keywords_does_not_exist():
    assert grep(__FOR_GREP_TEST_FILE_PATH, "hoge", "fuga") == []
    assert grep(__FOR_GREP_TEST_FILE_PATH, "hoge", "fuga") == list()


def test_grep_multiple_keywords_list_does_not_exist():
    assert grep(__FOR_GREP_TEST_FILE_PATH, *["hoge", "fuga"]) == []
    assert grep(__FOR_GREP_TEST_FILE_PATH, *["hoge", "fuga"]) == list()

###############
# grep_re test
###############


def test_grep_re_empty_file():
    assert grep_re(__EMPTY_FILE_PATH, "big") == []
    assert grep_re(__EMPTY_FILE_PATH, "big") == list()


def test_grep_re_keywords_none():
    with pytest.raises(TypeError):
        assert grep_re(__FOR_GREP_TEST_FILE_PATH, None)


def test_grep_re_one_keyword_exists():
    assert grep_re(__FOR_GREP_TEST_FILE_PATH, "^Just") == [
        {
            "no": 7,
            "text": "Just three stories."
        }
    ]


def test_grep_re_multiple_keywords_exist():
    assert grep_re(__FOR_GREP_TEST_FILE_PATH, "^I", "world.$") == [
        {
            "no": 1,
            "text": "I am honored to be with you today at your commencement from one of the finest universities in the world."
        }
    ]


def test_grep_re_multiple_keywords_list_exist():
    assert grep_re(__FOR_GREP_TEST_FILE_PATH, *["^I", "world.$"]) == [
        {
            "no": 1,
            "text": "I am honored to be with you today at your commencement from one of the finest universities in the world."
        }
    ]


def test_grep_re_one_keyword_does_not_exists():
    assert grep_re(__FOR_GREP_TEST_FILE_PATH, "^parents") == []
    assert grep_re(__FOR_GREP_TEST_FILE_PATH, "^parents") == list()


def test_grep_re_multiple_keywords_does_not_exist():
    assert grep_re(__FOR_GREP_TEST_FILE_PATH, "^parents", "today$") == []
    assert grep_re(__FOR_GREP_TEST_FILE_PATH, "^parents", "today$") == list()


def test_grep_re_multiple_keywords_list_does_not_exist():
    assert grep_re(__FOR_GREP_TEST_FILE_PATH, *["^parents", "today$"]) == []
    assert grep_re(__FOR_GREP_TEST_FILE_PATH, *
                   ["^parents", "today$"]) == list()


#################
# readlines test
#################


def test_readlines_file_path_none():
    with pytest.raises(TypeError):
        readlines(None)


def test_readlines_file_does_not_exist():
    with pytest.raises(FileNotFoundError):
        readlines("aaaaaaaaa")


def test_readlines_empty_file():
    assert readlines(__EMPTY_FILE_PATH) == []
    assert readlines(__EMPTY_FILE_PATH) == list()


def test_readlines_file_that_exist():
    assert readlines(__FOR_GREP_TEST_FILE_PATH) == [
        "I am honored to be with you today at your commencement from one of the finest universities in the world.",
        "I never graduated from college.",
        "Truth be told, this is the closest I’ve ever gotten to a college graduation.",
        "Today I want to tell you three stories from my life.",
        "That’s it.",
        "No big deal.",
        "Just three stories.",
        "The first story is about connecting the dots.",
        "I dropped out of Reed College after the first 6 months, but then stayed around as a drop-in for another 18 months or so before I really quit.",
        "So why did I drop out?",
        "It started before I was born.",
        "My biological mother was a young, unwed college graduate student, and she decided to put me up for adoption.",
        "She felt very strongly that I should be adopted by college graduates, so everything was all set for me to be adopted at birth by a lawyer and his wife.",
        "Except that when I popped out they decided at the last minute that they really wanted a girl.",
        "So my parents, who were on a waiting list, got a call in the middle of the night asking: “We have an unexpected baby boy; do you want him?” They said: “Of course.” My biological mother later found out that my mother had never graduated from college and that my father had never graduated from high school.",
        "She refused to sign the final adoption papers.",
        "She only relented a few months later when my parents promised that I would someday go to college."]
