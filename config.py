import os, random, string

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or \
        "".join(random.choices(string.ascii_letters + string.digits, k = 11))
