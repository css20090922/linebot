import builtins as _mod_builtins
import zmq.error as _mod_zmq_error

IPC_PATH_MAX_LEN = 0
InterruptedSystemCall = _mod_zmq_error.InterruptedSystemCall
class Socket(_mod_builtins.object):
    'Socket(context, socket_type)\n\n    A 0MQ socket.\n\n    These objects will generally be constructed via the socket() method of a Context object.\n    \n    Note: 0MQ Sockets are *not* threadsafe. **DO NOT** share them across threads.\n    \n    Parameters\n    ----------\n    context : Context\n        The 0MQ Context this Socket belongs to.\n    socket_type : int\n        The socket type, which can be any of the 0MQ socket types: \n        REQ, REP, PUB, SUB, PAIR, DEALER, ROUTER, PULL, PUSH, XPUB, XSUB.\n    \n    See Also\n    --------\n    .Context.socket : method for creating a socket bound to a Context.\n    '
    __class__ = Socket
    def __init__(self, context, socket_type):
        'Socket(context, socket_type)\n\n    A 0MQ socket.\n\n    These objects will generally be constructed via the socket() method of a Context object.\n    \n    Note: 0MQ Sockets are *not* threadsafe. **DO NOT** share them across threads.\n    \n    Parameters\n    ----------\n    context : Context\n        The 0MQ Context this Socket belongs to.\n    socket_type : int\n        The socket type, which can be any of the 0MQ socket types: \n        REQ, REP, PUB, SUB, PAIR, DEALER, ROUTER, PULL, PUSH, XPUB, XSUB.\n    \n    See Also\n    --------\n    .Context.socket : method for creating a socket bound to a Context.\n    '
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
    def _closed(self):
        pass
    
    def bind(self, addr):
        "s.bind(addr)\n\n        Bind the socket to an address.\n\n        This causes the socket to listen on a network port. Sockets on the\n        other side of this connection will use ``Socket.connect(addr)`` to\n        connect to this socket.\n\n        Parameters\n        ----------\n        addr : str\n            The address string. This has the form 'protocol://interface:port',\n            for example 'tcp://127.0.0.1:5555'. Protocols supported include\n            tcp, udp, pgm, epgm, inproc and ipc. If the address is unicode, it is\n            encoded to utf-8 first.\n        "
        pass
    
    def close(self, linger):
        's.close(linger=None)\n\n        Close the socket.\n\n        If linger is specified, LINGER sockopt will be set prior to closing.\n\n        This can be called to close the socket by hand. If this is not\n        called, the socket will automatically be closed when it is\n        garbage collected.\n        '
        pass
    
    @property
    def closed(self):
        pass
    
    def connect(self, addr):
        "s.connect(addr)\n\n        Connect to a remote 0MQ socket.\n\n        Parameters\n        ----------\n        addr : str\n            The address string. This has the form 'protocol://interface:port',\n            for example 'tcp://127.0.0.1:5555'. Protocols supported are\n            tcp, upd, pgm, inproc and ipc. If the address is unicode, it is\n            encoded to utf-8 first.\n        "
        pass
    
    @property
    def context(self):
        pass
    
    @property
    def copy_threshold(self):
        pass
    
    def disconnect(self, addr):
        "s.disconnect(addr)\n\n        Disconnect from a remote 0MQ socket (undoes a call to connect).\n        \n        .. versionadded:: libzmq-3.2\n        .. versionadded:: 13.0\n\n        Parameters\n        ----------\n        addr : str\n            The address string. This has the form 'protocol://interface:port',\n            for example 'tcp://127.0.0.1:5555'. Protocols supported are\n            tcp, upd, pgm, inproc and ipc. If the address is unicode, it is\n            encoded to utf-8 first.\n        "
        pass
    
    def get(self, option):
        's.get(option)\n\n        Get the value of a socket option.\n\n        See the 0MQ API documentation for details on specific options.\n\n        Parameters\n        ----------\n        option : int\n            The option to get.  Available values will depend on your\n            version of libzmq.  Examples include::\n            \n                zmq.IDENTITY, HWM, LINGER, FD, EVENTS\n\n        Returns\n        -------\n        optval : int or bytes\n            The value of the option as a bytestring or int.\n        '
        pass
    
    def join(self, group):
        'join(group)\n\n        Join a RADIO-DISH group\n\n        Only for DISH sockets.\n\n        libzmq and pyzmq must have been built with ZMQ_BUILD_DRAFT_API\n\n        .. versionadded:: 17\n        '
        pass
    
    def leave(self, group):
        'leave(group)\n\n        Leave a RADIO-DISH group\n\n        Only for DISH sockets.\n\n        libzmq and pyzmq must have been built with ZMQ_BUILD_DRAFT_API\n\n        .. versionadded:: 17\n        '
        pass
    
    def monitor(self, addr, events):
        's.monitor(addr, flags)\n\n        Start publishing socket events on inproc.\n        See libzmq docs for zmq_monitor for details.\n\n        While this function is available from libzmq 3.2,\n        pyzmq cannot parse monitor messages from libzmq prior to 4.0.\n\n        .. versionadded: libzmq-3.2\n        .. versionadded: 14.0\n\n        Parameters\n        ----------\n        addr : str\n            The inproc url used for monitoring. Passing None as\n            the addr will cause an existing socket monitor to be\n            deregistered.\n        events : int [default: zmq.EVENT_ALL]\n            The zmq event bitmask for which events will be sent to the monitor.\n        '
        pass
    
    def recv(self, flags, copy, track):
        's.recv(flags=0, copy=True, track=False)\n\n        Receive a message.\n\n        With flags=NOBLOCK, this raises :class:`ZMQError` if no messages have\n        arrived; otherwise, this waits until a message arrives.\n        See :class:`Poller` for more general non-blocking I/O.\n\n        Parameters\n        ----------\n        flags : int\n            0 or NOBLOCK.\n        copy : bool\n            Should the message be received in a copying or non-copying manner?\n            If False a Frame object is returned, if True a string copy of\n            message is returned.\n        track : bool\n            Should the message be tracked for notification that ZMQ has\n            finished with it? (ignored if copy=True)\n\n        Returns\n        -------\n        msg : bytes or Frame\n            The received message frame.  If `copy` is False, then it will be a Frame,\n            otherwise it will be bytes.\n\n        Raises\n        ------\n        ZMQError\n            for any of the reasons zmq_msg_recv might fail (including if\n            NOBLOCK is set and no new messages have arrived).\n        '
        pass
    
    def send(self, data, flags, copy, track):
        'Send a single zmq message frame on this socket.\n\n        This queues the message to be sent by the IO thread at a later time.\n\n        With flags=NOBLOCK, this raises :class:`ZMQError` if the queue is full;\n        otherwise, this waits until space is available.\n        See :class:`Poller` for more general non-blocking I/O.\n\n        Parameters\n        ----------\n        data : bytes, Frame, memoryview\n            The content of the message. This can be any object that provides\n            the Python buffer API (`memoryview(data)` can be called).\n        flags : int\n            0, NOBLOCK, SNDMORE, or NOBLOCK|SNDMORE.\n        copy : bool\n            Should the message be sent in a copying or non-copying manner.\n        track : bool\n            Should the message be tracked for notification that ZMQ has\n            finished with it? (ignored if copy=True)\n\n        Returns\n        -------\n        None : if `copy` or not track\n            None if message was sent, raises an exception otherwise.\n        MessageTracker : if track and not copy\n            a MessageTracker object, whose `pending` property will\n            be True until the send is completed.\n        \n        Raises\n        ------\n        TypeError\n            If a unicode object is passed\n        ValueError\n            If `track=True`, but an untracked Frame is passed.\n        ZMQError\n            for any of the reasons zmq_msg_send might fail (including\n            if NOBLOCK is set and the outgoing queue is full).\n        \n        '
        pass
    
    def set(self, option, optval):
        's.set(option, optval)\n\n        Set socket options.\n\n        See the 0MQ API documentation for details on specific options.\n\n        Parameters\n        ----------\n        option : int\n            The option to set.  Available values will depend on your\n            version of libzmq.  Examples include::\n\n                zmq.SUBSCRIBE, UNSUBSCRIBE, IDENTITY, HWM, LINGER, FD\n\n        optval : int or bytes\n            The value of the option to set.\n\n        Notes\n        -----\n        .. warning::\n\n            All options other than zmq.SUBSCRIBE, zmq.UNSUBSCRIBE and\n            zmq.LINGER only take effect for subsequent socket bind/connects.\n        '
        pass
    
    def unbind(self, addr):
        "s.unbind(addr)\n        \n        Unbind from an address (undoes a call to bind).\n        \n        .. versionadded:: libzmq-3.2\n        .. versionadded:: 13.0\n\n        Parameters\n        ----------\n        addr : str\n            The address string. This has the form 'protocol://interface:port',\n            for example 'tcp://127.0.0.1:5555'. Protocols supported are\n            tcp, upd, pgm, inproc and ipc. If the address is unicode, it is\n            encoded to utf-8 first.\n        "
        pass
    
    @property
    def underlying(self):
        'The address of the underlying libzmq socket'
        pass
    

ZMQBindError = _mod_zmq_error.ZMQBindError
ZMQError = _mod_zmq_error.ZMQError
__all__ = _mod_builtins.list()
__builtins__ = {}
__doc__ = '0MQ Socket class.'
__file__ = 'c:\\users\\twedw\\anaconda3\\lib\\site-packages\\zmq\\backend\\cython\\socket.cp37-win_amd64.pyd'
__name__ = 'zmq.backend.cython.socket'
__package__ = 'zmq.backend.cython'
def __reduce_cython__(self):
    pass

def __setstate_cython__(self, __pyx_state):
    pass

__test__ = _mod_builtins.dict()
def _check_version(min_version_info, msg):
    'Check for libzmq\n    \n    raises ZMQVersionError if current zmq version is not at least min_version\n    \n    min_version_info is a tuple of integers, and will be compared against zmq.zmq_version_info().\n    '
    pass

cPickle = None
