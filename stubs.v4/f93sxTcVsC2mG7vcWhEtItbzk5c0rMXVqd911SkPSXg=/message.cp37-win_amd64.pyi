import builtins as _mod_builtins
import threading as _mod_threading

Event = _mod_threading.Event
class Frame(_mod_builtins.object):
    __class__ = Frame
    def __copy__(self):
        'Create a shallow copy of the message.\n\n        This does not copy the contents of the Frame, just the pointer.\n        This will increment the 0MQ ref count of the message, but not\n        the ref count of the Python object. That is only done once when\n        the Python is first turned into a 0MQ message.\n        '
        pass
    
    def __init__(self):
        'Enforce signature'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return the length of the message in bytes.'
        return 0
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    def __str__(self):
        'Return the str form of the message.'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def buffer(self):
        'A read-only buffer view of the message contents.'
        pass
    
    @property
    def bytes(self):
        'The message content as a Python bytes object.\n\n        The first time this property is accessed, a copy of the message \n        contents is made. From then on that same copy of the message is\n        returned.\n        '
        pass
    
    def get(self, option):
        'Frame.get(option)\n\n        Get a Frame option or property.\n\n        See the 0MQ API documentation for zmq_msg_get and zmq_msg_gets\n        for details on specific options.\n\n        .. versionadded:: libzmq-3.2\n        .. versionadded:: 13.0\n\n        .. versionchanged:: 14.3\n            add support for zmq_msg_gets (requires libzmq-4.1)\n        .. versionchanged:: 17.0\n            Added support for `routing_id` and `group`.\n            Only available if draft API is enabled\n            with libzmq >= 4.2.\n        '
        pass
    
    @property
    def more(self):
        pass
    
    def set(self, option, value):
        'Frame.set(option, value)\n        \n        Set a Frame option.\n        \n        See the 0MQ API documentation for zmq_msg_set\n        for details on specific options.\n        \n        .. versionadded:: libzmq-3.2\n        .. versionadded:: 13.0\n        .. versionchanged:: 17.0\n            Added support for `routing_id` and `group`.\n            Only available if draft API is enabled\n            with libzmq >= 4.2.\n        '
        pass
    
    @property
    def tracker(self):
        pass
    
    @property
    def tracker_event(self):
        pass
    

Message = Frame
class MessageTracker(_mod_builtins.object):
    __class__ = MessageTracker
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

__all__ = _mod_builtins.list()
__builtins__ = {}
__doc__ = '0MQ Message related classes.'
__file__ = 'c:\\users\\twedw\\anaconda3\\lib\\site-packages\\zmq\\backend\\cython\\message.cp37-win_amd64.pyd'
__name__ = 'zmq.backend.cython.message'
__package__ = 'zmq.backend.cython'
def __reduce_cython__(self):
    pass

def __setstate_cython__(self, __pyx_state):
    pass

__test__ = _mod_builtins.dict()
def _check_version(min_version_info, msg):
    'Check for libzmq\n    \n    raises ZMQVersionError if current zmq version is not at least min_version\n    \n    min_version_info is a tuple of integers, and will be compared against zmq.zmq_version_info().\n    '
    pass

gc = None
