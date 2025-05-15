import random
import string

url_store = {}  # in-memory storage


def generate_code(length=6):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def shorten_url(original_url: str) -> str:
    code = generate_code()
    url_store[code] = original_url
    return code


def get_original_url(code: str) -> str | None:
    return url_store.get(code)
