Things Which Need Doing
=======================

* Write foad-server.py.
** A flask instance to act as an API for a remote instance of foad.py.
** Will call foad.py via the subprocess module.
** May be able to import parts of foad.py later instead of subprocess.
* Write foad-client.py.
** Standard command line script using requests module to access content served by foad-server.py.
** Essentially similar to the scripts to access the original FOAAS server.
