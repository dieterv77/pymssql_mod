#!/usr/bin/env python

import os
import sys
from setuptools import setup, Extension
from Cython.Distutils import build_ext

if sys.platform == 'win32':
    print ('ERROR: This version of pymssql is not support on windows')
    sys.exit(1)

else:
    include_dirs = [
        '/usr/local/include', '/usr/local/include/freetds',  # first local install
        '/usr/include', '/usr/include/freetds',   # some generic Linux paths
        '/usr/include/freetds_mssql',             # some versions of Mandriva 
        '/usr/local/freetds/include',             # FreeBSD
        '/usr/pkg/freetds/include'	              # NetBSD
    ]
    library_dirs = [
        '/usr/local/lib', '/usr/local/lib/freetds',
        '/usr/lib64',
        '/usr/lib', '/usr/lib/freetds',
        '/usr/lib/freetds_mssql', 
        '/usr/local/freetds/lib',
        '/usr/pkg/freetds/lib'
    ]
    libraries = [ "sybdb" ]   # on Mandriva you may have to change it to sybdb_mssql
    data_files = []

if sys.platform == 'darwin':
    fink = '/sw/'
    include_dirs.insert(0, fink + 'include')
    library_dirs.insert(0, fink + 'lib')

setup(
    name  = 'pymssql',
    version = '2.0.0',
    description = 'A simple database interface to MS-SQL for Python.',
    long_description = 'A simple database interface to MS-SQL for Python.',
    author = 'Damien Churchill',
    author_email = 'damoxc@gmail.com',
    license = 'LGPL',
    url = 'http://pymssql.sourceforge.net',
    py_modules = ['pymssql'],
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension('_mssql', ['_mssql.pyx'],
                             include_dirs = include_dirs,
                             library_dirs = library_dirs,
                             libraries = libraries)],
    data_files = data_files
)
