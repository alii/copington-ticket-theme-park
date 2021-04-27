def is_positive(string: str) -> bool:
    """
    Finds positive values in a string
    :param string: The string to find value in
    :return:
    """

    string = string.lower()
    positive_responses = ["yes", "yup", "sure", "of course", "y"]

    for response in positive_responses:
        if response in string:
            return True

    return False
