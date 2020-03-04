import builtins as _mod_builtins
import zmq.error as _mod_zmq_error

InterruptedSystemCall = _mod_zmq_error.InterruptedSystemCall
__all__ = _mod_builtins.list()
__builtins__ = {}
__doc__ = 'Python binding for 0MQ device function.'
__file__ = 'c:\\users\\twedw\\anaconda3\\lib\\site-packages\\zmq\\backend\\cython\\_device.cp37-win_amd64.pyd'
__name__ = 'zmq.backend.cython._device'
__package__ = 'zmq.backend.cython'
__test__ = _mod_builtins.dict()
def device(device_type, frontend, backend):
    'device(device_type, frontend, backend)\n\n    Start a zeromq device.\n    \n    .. deprecated:: libzmq-3.2\n        Use zmq.proxy\n\n    Parameters\n    ----------\n    device_type : (QUEUE, FORWARDER, STREAMER)\n        The type of device to start.\n    frontend : Socket\n        The Socket instance for the incoming traffic.\n    backend : Socket\n        The Socket instance for the outbound traffic.\n    '
    pass

def proxy(frontend, backend, capture):
    'proxy(frontend, backend, capture)\n    \n    Start a zeromq proxy (replacement for device).\n    \n    .. versionadded:: libzmq-3.2\n    .. versionadded:: 13.0\n    \n    Parameters\n    ----------\n    frontend : Socket\n        The Socket instance for the incoming traffic.\n    backend : Socket\n        The Socket instance for the outbound traffic.\n    capture : Socket (optional)\n        The Socket instance for capturing traffic.\n    '
    pass

