import os
import re


def grep(file_path: str, *keywords) -> list:
    """Grep command that is like grep command on Linux function.

    Parameters
    ----------
    file_path : str
        A file path to be processed
    keywords : multiple parameters or list
        Search keywords

    Returns
    -------
    list
        A list of objects consisting of line numbers and corresponding line text

    Examples
    --------
    >>> file_path = "test_dir/test.txt"
    >>> result = grep(file_path, "hoge", "fuga")
    result[
        {"no": 3, "text": "hogehogehoge"},
        {"no": 5, "text": "fugafugafuga"}
    ]
    """
    stripe_lines = readlines(file_path)
    return [{"no": i + 1, "text": line} for i, line in enumerate(stripe_lines)
            if all(word in line for word in keywords)]


def grep_re(file_path: str, *patterns) -> list:
    """Grep command that is like grep command on Linux function.

    Parameters
    ----------
    file_path : str
        A file path to be processed
    keywords : multiple parameters or list
        Search keywords (Regular expression)

    Returns
    -------
    list
        A list of objects consisting of line numbers and corresponding line text

    Examples
    --------
    >>> file_path = "test_dir/i_have_a_dream.txt"
    >>> result = grep(file_path, "^Five", "Proclamation.$")
    result[
        {"no": 1, "text": "Five score years ago, a great American, in whose symbolic shadow we stand today,"},
        {"no": 2, "text": "signed the Emancipation Proclamation."}
    ]
    """
    stripe_lines = readlines(file_path)
    return [{"no": i + 1, "text": line} for i, line in enumerate(stripe_lines)
            if all(re.search(pattern, line) for pattern in patterns)]


def readlines(file_path: str) -> list:
    """Read all lines of the file.

    Parameters
    ----------
    file_path : str
        A file path to be processed

    Returns
    -------
    list
        All lines of the file

    Examples
    --------
    >>> file_path = "test_dir/i_have_a_dream.txt"
    >>> result = readlines(file_path)
    result[
        "I am honored to be with you today at your commencement from ",
        "one of the finest universities in the world.",
        "I never graduated from college.",
        ...
    ]
    """
    with open(file_path) as f:
        stripe_lines = [line.rstrip(os.linesep) for line in f.readlines()]
    return stripe_lines
