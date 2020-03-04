import builtins as _mod_builtins
import zmq.error as _mod_zmq_error

InterruptedSystemCall = _mod_zmq_error.InterruptedSystemCall
__all__ = _mod_builtins.list()
__builtins__ = {}
__doc__ = 'Python binding for ZMQ steerable proxy function.'
__file__ = 'c:\\users\\twedw\\anaconda3\\lib\\site-packages\\zmq\\backend\\cython\\_proxy_steerable.cp37-win_amd64.pyd'
__name__ = 'zmq.backend.cython._proxy_steerable'
__package__ = 'zmq.backend.cython'
__test__ = _mod_builtins.dict()
def proxy_steerable(frontend, backend, capture, control):
    'proxy_steerable(frontend, backend, capture, control)\n\n    Start a zeromq proxy with control flow.\n\n    .. versionadded:: libzmq-4.1\n    .. versionadded:: 18.0\n\n    Parameters\n    ----------\n    frontend : Socket\n        The Socket instance for the incoming traffic.\n    backend : Socket\n        The Socket instance for the outbound traffic.\n    capture : Socket (optional)\n        The Socket instance for capturing traffic.\n    control : Socket (optional)\n        The Socket instance for control flow.\n    '
    pass

