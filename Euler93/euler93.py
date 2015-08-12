# $Id$
#
#  Copyright (C) 2005   Gregory P. Smith (greg@krypto.org)
#  Licensed to PSF under a Contributor Agreement.
#



# This tuple and __get_builtin_constructor() must be modified if a new
# always available algorithm is added.






def __get_builtin_constructor(name):
    try:
        if name in ('SHA1', 'sha1'):
            import _sha
            return _sha.new
        elif name in ('MD5', 'md5'):
            import _md5
            return _md5.new
        elif name in ('SHA256', 'sha256', 'SHA224', 'sha224'):
            import _sha256
            bs = name[3:]
            if bs == '256':
                return _sha256.sha256
            elif bs == '224':
                return _sha256.sha224
        elif name in ('SHA512', 'sha512', 'SHA384', 'sha384'):
            import _sha512
            bs = name[3:]
            if bs == '512':
                return _sha512.sha512
            elif bs == '384':
                return _sha512.sha384
    except ImportError:
        pass  # no extension module, this hash is unsupported.

    raise ValueError('unsupported hash type ' + name)


def __get_openssl_constructor(name):
    try:
        f = getattr(_hashlib, 'openssl_' + name)
        # Allow the C module to raise ValueError.  The function will be
        # defined but the hash not actually available thanks to OpenSSL.
        f()
        # Use the C function directly (very fast)
        return f
    except (AttributeError, ValueError):
        return __get_builtin_constructor(name)


def __py_new(name, string=''):

    return __get_builtin_constructor(name)(string)


def __hash_new(name, string=''):

    try:
        return _hashlib.new(name, string)
    except ValueError:
        # If the _hashlib module (OpenSSL) doesn't support the named
        # hash, try using our builtin implementations.
        # This allows for SHA224/256 and SHA384/512 support even though
        # the OpenSSL library prior to 0.9.8 doesn't provide them.
        return __get_builtin_constructor(name)(string)


try:
    import _hashlib
    new = __hash_new
    __get_hash = __get_openssl_constructor
    algorithms_available = algorithms_available.union(
        _hashlib.openssl_md_meth_names)
except ImportError:
    new = __py_new
    __get_hash = __get_builtin_constructor

for __func_name in __always_supported:
    # try them all, some may not work due to the OpenSSL
    # version not supporting that algorithm.
    try:
        globals()[__func_name] = __get_hash(__func_name)
    except ValueError:
        import logging
        logging.exception('code for hash %s was not found.', __func_name)


try:
    # OpenSSL's PKCS5_PBKDF2_HMAC requires OpenSSL 1.0+ with HMAC and SHA
    from _hashlib import pbkdf2_hmac
except ImportError:
    import binascii
    import struct

    _trans_5C = b"".join(chr(x ^ 0x5C) for x in range(256))
    _trans_36 = b"".join(chr(x ^ 0x36) for x in range(256))

    def pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None):

        if not isinstance(hash_name, str):
            raise TypeError(hash_name)

        if not isinstance(password, (bytes, bytearray)):
            password = bytes(buffer(password))
        if not isinstance(salt, (bytes, bytearray)):
            salt = bytes(buffer(salt))

        # Fast inline HMAC implementation
        inner = new(hash_name)
        outer = new(hash_name)
        blocksize = getattr(inner, 'block_size', 64)
        if len(password) > blocksize:
            password = new(hash_name, password).digest()
        password = password + b'\x00' * (blocksize - len(password))
        inner.update(password.translate(_trans_36))
        outer.update(password.translate(_trans_5C))

        def prf(msg, inner=inner, outer=outer):
            # PBKDF2_HMAC uses the password as key. We can re-use the same
            # digest objects and just update copies to skip initialization.
            icpy = inner.copy()
            ocpy = outer.copy()
            icpy.update(msg)
            ocpy.update(icpy.digest())
            return ocpy.digest()

        if iterations < 1:
            raise ValueError(iterations)
        if dklen is None:
            dklen = outer.digest_size
        if dklen < 1:
            raise ValueError(dklen)

        hex_format_string = "%%0%ix" % (new(hash_name).digest_size * 2)

        dkey = b''
        loop = 1
        while len(dkey) < dklen:
            prev = prf(salt + struct.pack(b'>I', loop))
            rkey = int(binascii.hexlify(prev), 16)
            for i in xrange(iterations - 1):
                prev = prf(prev)
                rkey ^= int(binascii.hexlify(prev), 16)
            loop += 1
            dkey += binascii.unhexlify(hex_format_string % rkey)

        return dkey[:dklen]

# Cleanup locals()
del __always_supported, __func_name, __get_hash
del __py_new, __hash_new, __get_openssl_constructor

dk = pbkdf2_hmac('sha256', b'password', b'salt', 100000)
binascii.hexlify(dk)


  