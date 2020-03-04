import builtins as _mod_builtins
import zmq.error as _mod_zmq_error

InterruptedSystemCall = _mod_zmq_error.InterruptedSystemCall
__all__ = _mod_builtins.list()
__builtins__ = {}
__doc__ = '0MQ polling related functions and classes.'
__file__ = 'c:\\users\\twedw\\anaconda3\\lib\\site-packages\\zmq\\backend\\cython\\_poll.cp37-win_amd64.pyd'
__name__ = 'zmq.backend.cython._poll'
__package__ = 'zmq.backend.cython'
__test__ = _mod_builtins.dict()
int_t = _mod_builtins.int
def monotonic():
    'monotonic() -> float\n\nMonotonic clock, cannot go backward.'
    return 1.0

def zmq_poll(sockets, timeout):
    'zmq_poll(sockets, timeout=-1)\n\n    Poll a set of 0MQ sockets, native file descs. or sockets.\n\n    Parameters\n    ----------\n    sockets : list of tuples of (socket, flags)\n        Each element of this list is a two-tuple containing a socket\n        and a flags. The socket may be a 0MQ socket or any object with\n        a ``fileno()`` method. The flags can be zmq.POLLIN (for detecting\n        for incoming messages), zmq.POLLOUT (for detecting that send is OK)\n        or zmq.POLLIN|zmq.POLLOUT for detecting both.\n    timeout : int\n        The number of milliseconds to poll for. Negative means no timeout.\n    '
    pass

