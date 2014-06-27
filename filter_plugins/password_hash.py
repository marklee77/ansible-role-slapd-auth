def ssha_password_hash(*a, **kw):
    from base64 import b64encode
    from hashlib import sha1
    password = a[0]
    salt = a[1]
    return '{SSHA}' + b64encode(sha1(password + salt).digest() + salt)

class FilterModule(object):
    ''' utility filter hash passwords '''

    def filters(self):
        return { 'ssha_password_hash' : ssha_password_hash }

