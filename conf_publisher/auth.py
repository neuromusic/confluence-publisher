from sys import version_info
from base64 import b64encode
from getpass import getpass

PY3 = version_info.major >= 3


def base64(string):
    if PY3:
        return b64encode(string.encode('utf8')).decode('utf8')
    return b64encode(string)


def parse_authentication(auth=None, user=None):
    if user is not None:
        password = getpass()
        return base64('%s:%s' % (user, password))
    return auth
