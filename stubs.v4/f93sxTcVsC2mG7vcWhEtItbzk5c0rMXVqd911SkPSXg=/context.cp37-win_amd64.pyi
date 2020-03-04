import builtins as _mod_builtins
import zmq.error as _mod_zmq_error

class Context(_mod_builtins.object):
    'Context(io_threads=1)\n\n    Manage the lifecycle of a 0MQ context.\n\n    Parameters\n    ----------\n    io_threads : int\n        The number of IO threads.\n    '
    __class__ = Context
    def __init__(self, io_threads=1):
        'Context(io_threads=1)\n\n    Manage the lifecycle of a 0MQ context.\n\n    Parameters\n    ----------\n    io_threads : int\n        The number of IO threads.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def closed(self):
        pass
    
    def get(self, option):
        'ctx.get(option)\n\n        Get the value of a context option.\n\n        See the 0MQ API documentation for zmq_ctx_get\n        for details on specific options.\n        \n        .. versionadded:: libzmq-3.2\n        .. versionadded:: 13.0\n\n        Parameters\n        ----------\n        option : int\n            The option to get.  Available values will depend on your\n            version of libzmq.  Examples include::\n            \n                zmq.IO_THREADS, zmq.MAX_SOCKETS\n            \n        Returns\n        -------\n        optval : int\n            The value of the option as an integer.\n        '
        pass
    
    def set(self, option, optval):
        'ctx.set(option, optval)\n\n        Set a context option.\n\n        See the 0MQ API documentation for zmq_ctx_set\n        for details on specific options.\n        \n        .. versionadded:: libzmq-3.2\n        .. versionadded:: 13.0\n\n        Parameters\n        ----------\n        option : int\n            The option to set.  Available values will depend on your\n            version of libzmq.  Examples include::\n            \n                zmq.IO_THREADS, zmq.MAX_SOCKETS\n        \n        optval : int\n            The value of the option to set.\n        '
        pass
    
    def term(self):
        'ctx.term()\n\n        Close or terminate the context.\n        \n        This can be called to close the context by hand. If this is not called,\n        the context will automatically be closed when it is garbage collected.\n        '
        pass
    
    @property
    def underlying(self):
        'The address of the underlying libzmq context'
        pass
    

InterruptedSystemCall = _mod_zmq_error.InterruptedSystemCall
ZMQError = _mod_zmq_error.ZMQError
__all__ = _mod_builtins.list()
__builtins__ = {}
__doc__ = '0MQ Context class.'
__file__ = 'c:\\users\\twedw\\anaconda3\\lib\\site-packages\\zmq\\backend\\cython\\context.cp37-win_amd64.pyd'
__name__ = 'zmq.backend.cython.context'
__package__ = 'zmq.backend.cython'
def __reduce_cython__(self):
    pass

def __setstate_cython__(self, __pyx_state):
    pass

__test__ = _mod_builtins.dict()
_instance = None
