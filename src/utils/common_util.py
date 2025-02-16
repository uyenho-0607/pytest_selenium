import random
import string


def cook_element(element: tuple, *custom):
    by, ele = element
    return by, ele.format(*custom)


def random_str(length=10):
    """Generate a random string of specified length."""
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    return ''.join(random.choices(characters, k=length))


def random_title(prefix="Auto Title"):
    return f"{prefix} - {random_str()}"


def random_sentence(prefix="Random sentence"):
    return f"{prefix} - {random_str()}"
