#!/usr/bin/env python
# _psosx.py

import os
import signal

import _psutil_osx


class Impl(object):

    def process_exists(self, pid):
        """Checks whether or not a process exists with the given PID."""
        return pid in self.get_pid_list()

    def get_process_info(self, pid):
        """Returns a tuple that can be passed to the psutil.ProcessInfo class
        constructor.
        """
        # XXX - figure out why it can't be imported globally (see r54)
        import psutil
        infoTuple = _psutil_osx.get_process_info(pid)
        return psutil.ProcessInfo(*infoTuple)

    def kill_process(self, pid, sig=signal.SIGKILL):
        """Terminates the process with the given PID."""
        os.kill(pid, sig)

    def get_pid_list(self):
        """Returns a list of PIDs currently running on the system."""
        return _psutil_osx.get_pid_list()

