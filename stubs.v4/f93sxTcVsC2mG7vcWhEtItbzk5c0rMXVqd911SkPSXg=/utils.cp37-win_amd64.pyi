import builtins as _mod_builtins
import zmq.error as _mod_zmq_error

ZMQError = _mod_zmq_error.ZMQError
__all__ = _mod_builtins.list()
__builtins__ = {}
__doc__ = '0MQ utils.'
__file__ = 'c:\\users\\twedw\\anaconda3\\lib\\site-packages\\zmq\\backend\\cython\\utils.cp37-win_amd64.pyd'
__name__ = 'zmq.backend.cython.utils'
__package__ = 'zmq.backend.cython'
__test__ = _mod_builtins.dict()
def _check_rc(rc, errno):
    'internal utility for checking zmq return condition\n    \n    and raising the appropriate Exception class\n    '
    pass

def _check_version(min_version_info, msg):
    'Check for libzmq\n    \n    raises ZMQVersionError if current zmq version is not at least min_version\n    \n    min_version_info is a tuple of integers, and will be compared against zmq.zmq_version_info().\n    '
    pass

def curve_keypair():
    'generate a Z85 keypair for use with zmq.CURVE security\n    \n    Requires libzmq (≥ 4.0) to have been built with CURVE support.\n    \n    .. versionadded:: libzmq-4.0\n    .. versionadded:: 14.0\n    \n    Returns\n    -------\n    (public, secret) : two bytestrings\n        The public and private keypair as 40 byte z85-encoded bytestrings.\n    '
    pass

def curve_public(secret_key):
    ' Compute the public key corresponding to a secret key for use\n    with zmq.CURVE security\n\n    Requires libzmq (≥ 4.2) to have been built with CURVE support.\n\n    Parameters\n    ----------\n    private\n        The private key as a 40 byte z85-encoded bytestring\n    Returns\n    -------\n    bytestring\n        The public key as a 40 byte z85-encoded bytestring.\n    '
    pass

def has(capability):
    "Check for zmq capability by name (e.g. 'ipc', 'curve')\n    \n    .. versionadded:: libzmq-4.1\n    .. versionadded:: 14.1\n    "
    pass

