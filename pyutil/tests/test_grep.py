import pytest
from pyutil.file import *


def test_grep_file_path_none():
    with pytest.raises(TypeError):
        grep(None, None)


def test_grep_file_does_not_exist():
    with pytest.raises(FileNotFoundError):
        grep("aaaaaaaaaaa", None)


def test_grep_empty_file():
    pass


def test_grep_keywords_none():
    pass


def test_grep_one_keyword_exists():
    pass


def test_grep_multiple_keywords_exist():
    pass


def test_grep_multiple_keywords_list_exist():
    pass


def test_grep_one_keyword_does_not_exists():
    pass


def test_grep_multiple_keywords_does_not_exist():
    pass


def test_grep_multiple_keywords_list_does_not_exist():
    pass


def test_grep_re_file_path_none():
    pass


def test_grep_re_file_does_not_exist():
    pass


def test_grep_re_empty_file():
    pass


def test_grep_re_keywords_none():
    pass


def test_grep_re_one_keyword_exists():
    pass


def test_grep_re_multiple_keywords_exist():
    pass


def test_grep_re_multiple_keywords_list_exist():
    pass


def test_grep_re_one_keyword_does_not_exists():
    pass


def test_grep_re_multiple_keywords_does_not_exist():
    pass


def test_grep_re_multiple_keywords_list_does_not_exist():
    pass


def test_readlines_file_path_none():
    pass


def test_readlines_file_does_not_exist():
    pass


def test_readlines_empty_file():
    pass


def test_readlines_file_that_exist():
    pass
