import _psutil_windows as _mod__psutil_windows

ABOVE_NORMAL_PRIORITY_CLASS = 32768
BELOW_NORMAL_PRIORITY_CLASS = 16384
ERROR_ACCESS_DENIED = 5
ERROR_INVALID_NAME = 123
ERROR_PRIVILEGE_NOT_HELD = 1314
ERROR_SERVICE_DOES_NOT_EXIST = 1060
HIGH_PRIORITY_CLASS = 128
IDLE_PRIORITY_CLASS = 64
INFINITE = -1
MIB_TCP_STATE_CLOSED = 1
MIB_TCP_STATE_CLOSE_WAIT = 8
MIB_TCP_STATE_CLOSING = 9
MIB_TCP_STATE_DELETE_TCB = 12
MIB_TCP_STATE_ESTAB = 5
MIB_TCP_STATE_FIN_WAIT1 = 6
MIB_TCP_STATE_FIN_WAIT2 = 7
MIB_TCP_STATE_LAST_ACK = 10
MIB_TCP_STATE_LISTEN = 2
MIB_TCP_STATE_SYN_RCVD = 4
MIB_TCP_STATE_SYN_SENT = 3
MIB_TCP_STATE_TIME_WAIT = 11
NORMAL_PRIORITY_CLASS = 32
PSUTIL_CONN_NONE = 128
REALTIME_PRIORITY_CLASS = 256
TimeoutAbandoned = _mod__psutil_windows.TimeoutAbandoned
TimeoutExpired = _mod__psutil_windows.TimeoutExpired
WINDOWS_10 = 100
WINDOWS_7 = 61
WINDOWS_8 = 62
WINDOWS_8_1 = 63
WINDOWS_SERVER_2003 = 52
WINDOWS_VISTA = 60
WINDOWS_XP = 51
WINVER = 100
__doc__ = None
__file__ = 'c:\\users\\twedw\\anaconda3\\lib\\site-packages\\psutil\\_psutil_windows.cp37-win_amd64.pyd'
__name__ = 'psutil_windows'
__package__ = 'psutil'
def boot_time():
    'Return the system boot time expressed in seconds since the epoch.'
    pass

def cpu_count_logical():
    'Returns the number of logical CPUs on the system'
    pass

def cpu_count_phys():
    'Returns the number of physical CPUs on the system'
    pass

def cpu_freq():
    'Return CPU frequency.'
    pass

def cpu_stats():
    'Return NICs stats.'
    pass

def cpu_times():
    'Return system cpu times as a list'
    pass

def disk_io_counters():
    'Return dict of tuples of disks I/O information.'
    pass

def disk_partitions():
    'Return disk partitions.'
    pass

def disk_usage():
    "Return path's disk total and free as a Python tuple."
    pass

def getloadavg():
    'Returns the emulated POSIX-like load average.'
    pass

def getpagesize():
    'Return system memory page size.'
    pass

def init_loadavg_counter():
    'Initializes the emulated load average calculator.'
    pass

def net_connections():
    'Return system-wide connections'
    pass

def net_if_addrs():
    'Return NICs addresses.'
    pass

def net_if_stats():
    'Return NICs stats.'
    pass

def net_io_counters():
    'Return dict of tuples of networks I/O information.'
    pass

def per_cpu_times():
    'Return system per-cpu times as a list of tuples'
    pass

def pid_exists():
    'Determine if the process exists in the current process list.'
    pass

def pids():
    'Returns a list of PIDs currently running on the system'
    pass

def ppid_map():
    'Return a {pid:ppid, ...} dict for all running processes'
    pass

def proc_cmdline():
    'Return process cmdline as a list of cmdline arguments'
    pass

def proc_cpu_affinity_get():
    'Return process CPU affinity as a bitmask.'
    pass

def proc_cpu_affinity_set():
    'Set process CPU affinity.'
    pass

def proc_cpu_times():
    'Return tuple of user/kern time for the given PID'
    pass

def proc_create_time():
    'Return a float indicating the process create time expressed in seconds since the epoch'
    pass

def proc_cwd():
    'Return process current working directory'
    pass

def proc_environ():
    'Return process environment data'
    pass

def proc_exe():
    'Return path of the process executable'
    pass

def proc_info():
    'Various process information'
    pass

def proc_io_counters():
    'Get process I/O counters.'
    pass

def proc_io_priority_get():
    'Return process IO priority.'
    pass

def proc_io_priority_set():
    'Set process IO priority.'
    pass

def proc_is_suspended():
    'Return True if one of the process threads is in a suspended state'
    pass

def proc_kill():
    'Kill the process identified by the given PID'
    pass

def proc_memory_info():
    'Return a tuple of process memory information'
    pass

def proc_memory_maps():
    "Return a list of process's memory mappings"
    pass

def proc_memory_uss():
    'Return the USS of the process'
    pass

def proc_name():
    'Return process name'
    pass

def proc_num_handles():
    'Return the number of handles opened by process.'
    pass

def proc_open_files():
    'Return files opened by process'
    pass

def proc_priority_get():
    'Return process priority.'
    pass

def proc_priority_set():
    'Set process priority.'
    pass

def proc_suspend_or_resume():
    'Suspend or resume a process'
    pass

def proc_threads():
    'Return process threads information as a list of tuple'
    pass

def proc_username():
    'Return the username of a process'
    pass

def proc_wait():
    'Wait for process to terminate and return its exit code.'
    pass

def sensors_battery():
    'Return battery metrics usage.'
    pass

def set_testing():
    'Set psutil in testing mode'
    pass

def users():
    'Return a list of currently connected users.'
    pass

version = 563
def virtual_mem():
    'Return the total amount of physical memory, in bytes'
    pass

def win32_QueryDosDevice():
    'QueryDosDevice binding'
    pass

def winservice_enumerate():
    'List all services'
    pass

def winservice_query_config():
    'Return service config'
    pass

def winservice_query_descr():
    'Return the description of a service'
    pass

def winservice_query_status():
    'Return service config'
    pass

def winservice_start():
    'Start a service'
    pass

def winservice_stop():
    'Stop a service'
    pass

